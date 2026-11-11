#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <sys/resource.h>
#include <vector>

using U = std::uint64_t;

struct Row {
  U global_index;
  std::array<U, 6> names;
  std::array<U, 3> canonical;
  std::array<U, 3> physical;
  std::array<U, 2> canonical_syndrome;
  std::array<U, 2> physical_syndrome;
  U canonical_logical;
  U physical_logical;
};

struct Triple {
  std::array<std::uint16_t, 3> index;
  std::array<U, 6> names;
  std::array<U, 3> canonical;
  std::array<U, 3> physical;
  std::array<U, 2> canonical_syndrome;
  std::array<U, 2> physical_syndrome;
  U canonical_logical;
  U physical_logical;
};

struct NameKey {
  std::array<U, 6> words;
  bool operator<(NameKey const &other) const { return words < other.words; }
};

struct Eligible {
  std::array<U, 3> canonical;
  std::array<U, 3> physical;
  std::array<U, 2> canonical_syndrome;
  std::array<U, 2> physical_syndrome;
  U canonical_logical;
  U physical_logical;
  U multiplicity;
  std::array<U, 6> first_indices;
};

static U choose_checked(U n, U k) {
  if (k > n) return 0;
  if (k > n - k) k = n - k;
  __uint128_t value = 1;
  for (U i = 1; i <= k; ++i) {
    value = value * (n - k + i) / i;
    if (value > std::numeric_limits<U>::max()) throw std::overflow_error("binomial overflow");
  }
  return static_cast<U>(value);
}

static U read_le64(std::ifstream &in) {
  unsigned char bytes[8];
  in.read(reinterpret_cast<char *>(bytes), 8);
  if (!in) throw std::runtime_error("truncated input");
  U value = 0;
  for (int i = 0; i < 8; ++i) value |= U(bytes[i]) << (8 * i);
  return value;
}

static void write_le64(std::ofstream &out, U value) {
  unsigned char bytes[8];
  for (int i = 0; i < 8; ++i) bytes[i] = static_cast<unsigned char>((value >> (8 * i)) & 0xffU);
  out.write(reinterpret_cast<char *>(bytes), 8);
  if (!out) throw std::runtime_error("output write failure");
}

template <std::size_t N>
static std::array<U, N> xor3(std::array<U, N> const &a, std::array<U, N> const &b,
                             std::array<U, N> const &c) {
  std::array<U, N> result{};
  for (std::size_t i = 0; i < N; ++i) result[i] = a[i] ^ b[i] ^ c[i];
  return result;
}

template <std::size_t N>
static std::array<U, N> xor2(std::array<U, N> const &a, std::array<U, N> const &b) {
  std::array<U, N> result{};
  for (std::size_t i = 0; i < N; ++i) result[i] = a[i] ^ b[i];
  return result;
}

template <std::size_t N>
static int popcount(std::array<U, N> const &a) {
  int result = 0;
  for (U value : a) result += __builtin_popcountll(value);
  return result;
}

static void add256(std::array<U, 4> &accumulator, U value, int limb) {
  __uint128_t sum = static_cast<__uint128_t>(accumulator[limb]) + value;
  accumulator[limb] = static_cast<U>(sum);
  U carry = static_cast<U>(sum >> 64);
  for (int i = limb + 1; carry && i < 4; ++i) {
    sum = static_cast<__uint128_t>(accumulator[i]) + carry;
    accumulator[i] = static_cast<U>(sum);
    carry = static_cast<U>(sum >> 64);
  }
}

static std::string hex256(std::array<U, 4> const &value) {
  std::ostringstream out;
  out << std::hex << std::setfill('0');
  for (int i = 3; i >= 0; --i) out << std::setw(16) << value[i];
  return out.str();
}

template <class T>
static std::string json_array(std::vector<T> const &values) {
  std::ostringstream out;
  out << '[';
  for (std::size_t i = 0; i < values.size(); ++i) {
    if (i) out << ',';
    out << values[i];
  }
  out << ']';
  return out.str();
}

static std::string histogram_pairs(std::map<U, U> const &histogram) {
  std::ostringstream out;
  out << '[';
  bool first = true;
  for (auto const &entry : histogram) {
    if (!first) out << ',';
    first = false;
    out << entry.first << ',' << entry.second;
  }
  out << ']';
  return out.str();
}

static std::array<U, 2> canonical_key(Triple const &triple) { return triple.canonical_syndrome; }
static std::array<U, 2> physical_key(Triple const &triple) { return triple.physical_syndrome; }
static std::array<U, 4> combined_key(Triple const &triple) {
  return {triple.canonical_syndrome[0], triple.canonical_syndrome[1],
          triple.physical_syndrome[0], triple.physical_syndrome[1]};
}

template <std::size_t N, class KeyFunction>
static U count_separated_equal_pairs(std::vector<Triple> const &triples, KeyFunction key,
                                     std::map<U, U> &group_histogram,
                                     std::array<U, 4> &checksum) {
  std::vector<std::uint32_t> order(triples.size());
  for (std::uint32_t i = 0; i < order.size(); ++i) order[i] = i;
  std::sort(order.begin(), order.end(), [&](std::uint32_t a, std::uint32_t b) {
    auto ka = key(triples[a]);
    auto kb = key(triples[b]);
    if (ka != kb) return ka < kb;
    return triples[a].index < triples[b].index;
  });
  U count = 0;
  std::size_t begin = 0;
  while (begin < order.size()) {
    std::size_t end = begin + 1;
    auto group_key = key(triples[order[begin]]);
    while (end < order.size() && key(triples[order[end]]) == group_key) ++end;
    U size = static_cast<U>(end - begin);
    group_histogram[size]++;
    std::vector<std::uint16_t> maxima;
    maxima.reserve(size);
    for (std::size_t pos = begin; pos < end; ++pos) maxima.push_back(triples[order[pos]].index[2]);
    std::sort(maxima.begin(), maxima.end());
    for (std::size_t pos = begin; pos < end; ++pos) {
      U add = static_cast<U>(std::lower_bound(maxima.begin(), maxima.end(), triples[order[pos]].index[0]) - maxima.begin());
      count += add;
      add256(checksum, add, 0);
      add256(checksum, static_cast<U>(triples[order[pos]].index[0]) + 1, 1);
    }
    begin = end;
  }
  return count;
}

int main(int argc, char **argv) {
  if (argc != 5) {
    std::cerr << "usage: order6_mitm INPUT ELIGIBLE SUMMARY SECTOR\n";
    return 2;
  }
  auto started = std::chrono::steady_clock::now();
  std::string input_path = argv[1], eligible_path = argv[2], summary_path = argv[3], sector = argv[4];
  std::ifstream input(input_path, std::ios::binary);
  if (!input) throw std::runtime_error("cannot open input");
  unsigned char magic[16];
  input.read(reinterpret_cast<char *>(magic), 16);
  unsigned char expected_magic[16] = {'C','D','R','9','8','O','5','V','1',0,0,0,0,0,0,0};
  if (!input || std::memcmp(magic, expected_magic, 16) != 0) throw std::runtime_error("bad magic");
  U n = read_le64(input);
  if (n > std::numeric_limits<std::uint16_t>::max()) throw std::runtime_error("index width overflow");
  std::vector<Row> rows(n);
  for (Row &row : rows) {
    row.global_index = read_le64(input);
    for (U &x : row.names) x = read_le64(input);
    for (U &x : row.canonical) x = read_le64(input);
    for (U &x : row.physical) x = read_le64(input);
    for (U &x : row.canonical_syndrome) x = read_le64(input);
    for (U &x : row.physical_syndrome) x = read_le64(input);
    row.canonical_logical = read_le64(input);
    row.physical_logical = read_le64(input);
    if ((row.names[5] >> 40) || (row.canonical[2] >> 16) || (row.physical[2] >> 16) ||
        (row.canonical_syndrome[1] >> 8) || (row.physical_syndrome[1] >> 8) ||
        (row.canonical_logical >> 12) || (row.physical_logical >> 12))
      throw std::runtime_error("unused high bits nonzero");
  }
  char trailing;
  if (input.read(&trailing, 1)) throw std::runtime_error("trailing input");

  U triple_expected = choose_checked(n, 3);
  U full_domain = choose_checked(n, 6);
  std::vector<Triple> triples;
  triples.reserve(triple_expected);
  std::array<U, 4> triple_checksum{};
  for (U a = 0; a + 2 < n; ++a) {
    for (U b = a + 1; b + 1 < n; ++b) {
      for (U c = b + 1; c < n; ++c) {
        Row const &A = rows[a], &B = rows[b], &C = rows[c];
        Triple triple{
          {static_cast<std::uint16_t>(a), static_cast<std::uint16_t>(b), static_cast<std::uint16_t>(c)},
          xor3(A.names, B.names, C.names), xor3(A.canonical, B.canonical, C.canonical),
          xor3(A.physical, B.physical, C.physical),
          xor3(A.canonical_syndrome, B.canonical_syndrome, C.canonical_syndrome),
          xor3(A.physical_syndrome, B.physical_syndrome, C.physical_syndrome),
          A.canonical_logical ^ B.canonical_logical ^ C.canonical_logical,
          A.physical_logical ^ B.physical_logical ^ C.physical_logical
        };
        triples.push_back(triple);
        add256(triple_checksum, (a + 1) * 3 + (b + 1) * 5 + (c + 1) * 7, 0);
        for (std::size_t i = 0; i < 6; ++i) add256(triple_checksum, triple.names[i], i & 3);
        for (std::size_t i = 0; i < 2; ++i) {
          add256(triple_checksum, triple.canonical_syndrome[i], (i + 1) & 3);
          add256(triple_checksum, triple.physical_syndrome[i], (i + 2) & 3);
        }
      }
    }
  }
  if (triples.size() != triple_expected) throw std::runtime_error("triple domain count mismatch");

  std::map<U, U> canonical_groups, physical_groups, combined_groups;
  std::array<U, 4> canonical_pair_checksum{}, physical_pair_checksum{};
  U canonical_zero = count_separated_equal_pairs<2>(triples, canonical_key, canonical_groups, canonical_pair_checksum);
  U physical_zero = count_separated_equal_pairs<2>(triples, physical_key, physical_groups, physical_pair_checksum);

  std::vector<std::uint32_t> order(triples.size());
  for (std::uint32_t i = 0; i < order.size(); ++i) order[i] = i;
  std::sort(order.begin(), order.end(), [&](std::uint32_t a, std::uint32_t b) {
    auto ka = combined_key(triples[a]);
    auto kb = combined_key(triples[b]);
    if (ka != kb) return ka < kb;
    return triples[a].index < triples[b].index;
  });

  U combined_zero = 0, eligible_occurrences = 0, conservative_valid_occurrences = 0;
  std::vector<U> name_weight_histogram(61), canonical_support_histogram(145), physical_support_histogram(145);
  std::vector<U> canonical_logical_histogram(4096), physical_logical_histogram(4096);
  std::array<U, 4> combined_checksum{};
  std::map<NameKey, Eligible> eligible;
  std::size_t begin = 0;
  while (begin < order.size()) {
    std::size_t end = begin + 1;
    auto key = combined_key(triples[order[begin]]);
    while (end < order.size() && combined_key(triples[order[end]]) == key) ++end;
    U group_size = static_cast<U>(end - begin);
    combined_groups[group_size]++;
    std::vector<std::uint32_t> lower(order.begin() + begin, order.begin() + end);
    std::sort(lower.begin(), lower.end(), [&](std::uint32_t a, std::uint32_t b) {
      if (triples[a].index[2] != triples[b].index[2]) return triples[a].index[2] < triples[b].index[2];
      return triples[a].index < triples[b].index;
    });
    for (std::size_t up = begin; up < end; ++up) {
      Triple const &upper = triples[order[up]];
      for (std::uint32_t lower_id : lower) {
        Triple const &lo = triples[lower_id];
        if (lo.index[2] >= upper.index[0]) break;
        ++combined_zero;
        auto names = xor2(lo.names, upper.names);
        auto canonical = xor2(lo.canonical, upper.canonical);
        auto physical = xor2(lo.physical, upper.physical);
        auto canonical_syndrome = xor2(lo.canonical_syndrome, upper.canonical_syndrome);
        auto physical_syndrome = xor2(lo.physical_syndrome, upper.physical_syndrome);
        U canonical_logical = lo.canonical_logical ^ upper.canonical_logical;
        U physical_logical = lo.physical_logical ^ upper.physical_logical;
        if (canonical_syndrome != std::array<U, 2>{0, 0} || physical_syndrome != std::array<U, 2>{0, 0})
          throw std::runtime_error("combined-key equality defect");
        int named_weight = popcount(names), canonical_weight = popcount(canonical), physical_weight = popcount(physical);
        if (named_weight > 60 || canonical_weight > 144 || physical_weight > 144 ||
            canonical_logical >= 4096 || physical_logical >= 4096)
          throw std::runtime_error("histogram range defect");
        name_weight_histogram[named_weight]++;
        canonical_support_histogram[canonical_weight]++;
        physical_support_histogram[physical_weight]++;
        canonical_logical_histogram[canonical_logical]++;
        physical_logical_histogram[physical_logical]++;
        std::array<U, 6> indices = {lo.index[0], lo.index[1], lo.index[2],
                                    upper.index[0], upper.index[1], upper.index[2]};
        add256(combined_checksum, (indices[0] + 1) * 3 + (indices[1] + 1) * 5 +
                                      (indices[2] + 1) * 7 + (indices[3] + 1) * 11 +
                                      (indices[4] + 1) * 13 + (indices[5] + 1) * 17, 0);
        for (std::size_t i = 0; i < 6; ++i) add256(combined_checksum, names[i], i & 3);
        for (std::size_t i = 0; i < 3; ++i) {
          add256(combined_checksum, canonical[i], (i + 1) & 3);
          add256(combined_checksum, physical[i], (i + 2) & 3);
        }
        add256(combined_checksum, canonical_logical, 2);
        add256(combined_checksum, physical_logical, 3);
        if (named_weight >= 1 && named_weight <= 10) {
          ++eligible_occurrences;
          NameKey name_key{names};
          auto found = eligible.find(name_key);
          if (found == eligible.end()) {
            eligible.emplace(name_key, Eligible{canonical, physical, canonical_syndrome, physical_syndrome,
                                                canonical_logical, physical_logical, 1, indices});
          } else {
            Eligible &stored = found->second;
            if (stored.canonical != canonical || stored.physical != physical ||
                stored.canonical_syndrome != canonical_syndrome || stored.physical_syndrome != physical_syndrome ||
                stored.canonical_logical != canonical_logical || stored.physical_logical != physical_logical)
              throw std::runtime_error("same full named mask has unequal physical effect");
            ++stored.multiplicity;
          }
          if (canonical_logical != 0 && physical_logical != 0 && canonical_logical == physical_logical)
            ++conservative_valid_occurrences;
        }
      }
    }
    begin = end;
  }
  if (combined_zero > canonical_zero || combined_zero > physical_zero || combined_zero > full_domain)
    throw std::runtime_error("candidate count bound defect");
  auto sum_histogram = [](std::vector<U> const &hist) {
    __uint128_t sum = 0;
    for (U value : hist) sum += value;
    if (sum > std::numeric_limits<U>::max()) throw std::overflow_error("histogram sum overflow");
    return static_cast<U>(sum);
  };
  for (auto const *hist : {&name_weight_histogram, &canonical_support_histogram, &physical_support_histogram,
                           &canonical_logical_histogram, &physical_logical_histogram})
    if (sum_histogram(*hist) != combined_zero) throw std::runtime_error("histogram sum mismatch");

  std::ofstream eligible_output(eligible_path, std::ios::binary);
  unsigned char output_magic[16] = {'C','D','R','1','0','0','O','6','V','1',0,0,0,0,0,0};
  eligible_output.write(reinterpret_cast<char *>(output_magic), 16);
  write_le64(eligible_output, static_cast<U>(eligible.size()));
  U unique_valid = 0, maximum_multiplicity = 0;
  std::map<U, U> multiplicity_histogram;
  for (auto const &entry : eligible) {
    NameKey const &name_key = entry.first;
    Eligible const &value = entry.second;
    for (U x : name_key.words) write_le64(eligible_output, x);
    for (U x : value.canonical) write_le64(eligible_output, x);
    for (U x : value.physical) write_le64(eligible_output, x);
    for (U x : value.canonical_syndrome) write_le64(eligible_output, x);
    for (U x : value.physical_syndrome) write_le64(eligible_output, x);
    write_le64(eligible_output, value.canonical_logical);
    write_le64(eligible_output, value.physical_logical);
    write_le64(eligible_output, value.multiplicity);
    for (U x : value.first_indices) write_le64(eligible_output, x);
    multiplicity_histogram[value.multiplicity]++;
    maximum_multiplicity = std::max(maximum_multiplicity, value.multiplicity);
    if (value.canonical_logical != 0 && value.physical_logical != 0 &&
        value.canonical_logical == value.physical_logical) ++unique_valid;
  }
  eligible_output.close();

  struct rusage usage{};
  if (getrusage(RUSAGE_SELF, &usage) != 0) throw std::runtime_error("getrusage failed");
  double seconds = std::chrono::duration<double>(std::chrono::steady_clock::now() - started).count();
  std::ofstream summary(summary_path);
  summary << "{\n"
          << "  \"schema\": \"circdist-round100-order6-mitm-census-v1\",\n"
          << "  \"status\": \"PASS\",\n"
          << "  \"sector\": \"" << sector << "\",\n"
          << "  \"selector_count\": " << n << ",\n"
          << "  \"triple_count_expected\": " << triple_expected << ",\n"
          << "  \"triple_count_enumerated\": " << triples.size() << ",\n"
          << "  \"full_six_distinct_domain_closed_form\": " << full_domain << ",\n"
          << "  \"full_six_distinct_domain_streamed\": false,\n"
          << "  \"exact_reduction\": \"unique lower-three/upper-three split; a six-tuple has zero syndrome iff the two complete triple syndrome vectors are equal\",\n"
          << "  \"canonical_syndrome_zero_six_tuples\": " << canonical_zero << ",\n"
          << "  \"physical_syndrome_zero_six_tuples\": " << physical_zero << ",\n"
          << "  \"combined_syndrome_zero_six_tuples\": " << combined_zero << ",\n"
          << "  \"eligible_named_weight_1_to_10_occurrences\": " << eligible_occurrences << ",\n"
          << "  \"unique_eligible_named_results\": " << eligible.size() << ",\n"
          << "  \"conservative_source_valid_occurrences\": " << conservative_valid_occurrences << ",\n"
          << "  \"unique_conservative_source_valid_results\": " << unique_valid << ",\n"
          << "  \"maximum_eligible_multiplicity\": " << maximum_multiplicity << ",\n"
          << "  \"eligible_multiplicity_histogram_flat_pairs\": " << histogram_pairs(multiplicity_histogram) << ",\n"
          << "  \"canonical_triple_key_group_histogram_flat_pairs\": " << histogram_pairs(canonical_groups) << ",\n"
          << "  \"physical_triple_key_group_histogram_flat_pairs\": " << histogram_pairs(physical_groups) << ",\n"
          << "  \"combined_triple_key_group_histogram_flat_pairs\": " << histogram_pairs(combined_groups) << ",\n"
          << "  \"combined_zero_named_weight_histogram\": " << json_array(name_weight_histogram) << ",\n"
          << "  \"combined_zero_canonical_support_weight_histogram\": " << json_array(canonical_support_histogram) << ",\n"
          << "  \"combined_zero_physical_support_weight_histogram\": " << json_array(physical_support_histogram) << ",\n"
          << "  \"combined_zero_canonical_logical_action_histogram\": " << json_array(canonical_logical_histogram) << ",\n"
          << "  \"combined_zero_physical_logical_action_histogram\": " << json_array(physical_logical_histogram) << ",\n"
          << "  \"triple_checksum_mod_2_256\": \"" << hex256(triple_checksum) << "\",\n"
          << "  \"canonical_pair_count_checksum_mod_2_256\": \"" << hex256(canonical_pair_checksum) << "\",\n"
          << "  \"physical_pair_count_checksum_mod_2_256\": \"" << hex256(physical_pair_checksum) << "\",\n"
          << "  \"combined_candidate_checksum_mod_2_256\": \"" << hex256(combined_checksum) << "\",\n"
          << "  \"equality_semantics\": \"std::array lexicographic equality/order over all syndrome words; no hash table participates\",\n"
          << "  \"binary_io\": \"explicit bytewise little-endian uint64; unused high bits checked zero\",\n"
          << "  \"counter_semantics\": \"uint64 observed counters; binomial arithmetic in checked unsigned 128-bit\",\n"
          << "  \"sizeof_triple_bytes\": " << sizeof(Triple) << ",\n"
          << "  \"peak_rss_bytes_macos\": " << usage.ru_maxrss << ",\n"
          << "  \"seconds\": " << std::fixed << std::setprecision(6) << seconds << "\n"
          << "}\n";
  summary.close();
  std::cout << "ORDER6_MITM_PASS " << sector << ' ' << n << ' ' << full_domain << ' '
            << combined_zero << ' ' << eligible_occurrences << ' ' << eligible.size() << ' '
            << conservative_valid_occurrences << ' ' << unique_valid << '\n';
  return 0;
}
