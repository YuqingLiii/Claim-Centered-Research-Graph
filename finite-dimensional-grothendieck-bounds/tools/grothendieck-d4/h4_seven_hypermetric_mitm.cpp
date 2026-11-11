#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

namespace {

constexpr int kCoordinates = 600;
constexpr int kFaces = 4800;
constexpr int kLiterals = 1110;
constexpr int kSignatureFaces = 48;
constexpr std::uint64_t kMagic = 0x4434534556454e31ULL;  // "D4SEVEN1"

struct Record {
  std::uint64_t hash;
  std::uint64_t code;
};

struct FullRecord {
  std::uint64_t parity;
  std::uint64_t majority;
  std::uint64_t code;
};

std::uint64_t mix64(std::uint64_t x) {
  x += 0x9e3779b97f4a7c15ULL;
  x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
  x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
  return x ^ (x >> 31);
}

std::uint64_t rotate_left(std::uint64_t x, unsigned amount) {
  return (x << amount) | (x >> (64 - amount));
}

template <class T>
void read_exact(std::ifstream& input, T* destination, std::size_t count) {
  input.read(reinterpret_cast<char*>(destination), sizeof(T) * count);
  if (!input) throw std::runtime_error("truncated input");
}

std::array<int, 3> unpack(std::uint64_t code) {
  constexpr std::uint64_t mask = (1ULL << 11) - 1;
  return {static_cast<int>(code & mask),
          static_cast<int>((code >> 11) & mask),
          static_cast<int>((code >> 22) & mask)};
}

std::pair<std::uint64_t, std::uint64_t> signature(
    const std::array<int, 3>& triple,
    const std::vector<std::uint64_t>& positive_masks) {
  const std::uint64_t a = positive_masks[triple[0]];
  const std::uint64_t b = positive_masks[triple[1]];
  const std::uint64_t c = positive_masks[triple[2]];
  const std::uint64_t parity = a ^ b ^ c;
  const std::uint64_t majority = (a & b) | (a & c) | (b & c);
  return {parity, majority};
}

bool cross_compatible(const std::array<int, 3>& first,
                      const std::array<int, 3>& second,
                      const std::vector<std::uint16_t>& coordinate,
                      const std::vector<std::uint8_t>& conflict) {
  for (int u : first) {
    const int i = coordinate[u];
    for (int v : second) {
      const int j = coordinate[v];
      if (conflict[i * kCoordinates + j]) return false;
    }
  }
  return true;
}

bool all_face_conditions(const std::array<int, 3>& first,
                         const std::array<int, 3>& second,
                         const std::vector<std::uint16_t>& coordinate,
                         const std::vector<std::int8_t>& literal_sign,
                         const std::vector<std::int8_t>& face_sign) {
  // The candidate is +e_0 plus `first` minus `second`.  The first 48 face
  // equations hold by the equal-signature grouping, so start at row 48.
  for (int row = kSignatureFaces; row < kFaces; ++row) {
    const std::int8_t* signs = &face_sign[row * kCoordinates];
    int fixed_sum = signs[0];
    int free_count = (signs[0] == 0);
    for (int literal : first) {
      const int value = signs[coordinate[literal]];
      if (value == 0) {
        ++free_count;
      } else {
        fixed_sum += literal_sign[literal] * value;
      }
    }
    for (int literal : second) {
      const int value = signs[coordinate[literal]];
      if (value == 0) {
        ++free_count;
      } else {
        fixed_sum -= literal_sign[literal] * value;
      }
    }
    if (free_count > 1 || std::abs(fixed_sum) != 1 - free_count) return false;
  }
  return true;
}

}  // namespace

int main(int argc, char** argv) {
  try {
    if (argc != 2) throw std::runtime_error("usage: checker INPUT.bin");
    std::ifstream input(argv[1], std::ios::binary);
    if (!input) throw std::runtime_error("cannot open input");
    std::uint64_t magic = 0;
    read_exact(input, &magic, 1);
    if (magic != kMagic) throw std::runtime_error("input magic mismatch");

    std::vector<std::int8_t> face_sign(kFaces * kCoordinates);
    std::vector<std::uint8_t> conflict(kCoordinates * kCoordinates);
    std::vector<std::uint16_t> coordinate(kLiterals);
    std::vector<std::int8_t> literal_sign(kLiterals);
    read_exact(input, face_sign.data(), face_sign.size());
    read_exact(input, conflict.data(), conflict.size());
    read_exact(input, coordinate.data(), coordinate.size());
    read_exact(input, literal_sign.data(), literal_sign.size());
    char extra;
    if (input.read(&extra, 1)) throw std::runtime_error("trailing input bytes");

    std::vector<std::uint64_t> positive_masks(kLiterals, 0);
    for (int literal = 0; literal < kLiterals; ++literal) {
      std::uint64_t mask = 0;
      for (int row = 0; row < kSignatureFaces; ++row) {
        const int value = face_sign[row * kCoordinates + coordinate[literal]] *
                          literal_sign[literal];
        if (value == 0) throw std::runtime_error("zero in literal signature");
        if (value > 0) mask |= 1ULL << row;
      }
      positive_masks[literal] = mask;
    }

    // A 200-million-record reserve is deliberately conservative.  Each
    // record is 16 bytes and the machine used for the certificate has ample
    // RAM; the exact emitted count below is part of the replay census.
    std::vector<Record> records;
    records.reserve(200000000ULL);
    for (int u = 0; u < kLiterals; ++u) {
      const int i = coordinate[u];
      for (int v = u + 1; v < kLiterals; ++v) {
        const int j = coordinate[v];
        if (conflict[i * kCoordinates + j]) continue;
        for (int w = v + 1; w < kLiterals; ++w) {
          const int k = coordinate[w];
          if (conflict[i * kCoordinates + k] ||
              conflict[j * kCoordinates + k]) {
            continue;
          }
          const std::uint64_t a = positive_masks[u];
          const std::uint64_t b = positive_masks[v];
          const std::uint64_t c = positive_masks[w];
          const std::uint64_t parity = a ^ b ^ c;
          const std::uint64_t majority = (a & b) | (a & c) | (b & c);
          const std::uint64_t hash =
              mix64(parity ^ rotate_left(majority, 23));
          const std::uint64_t code = static_cast<std::uint64_t>(u) |
                                     (static_cast<std::uint64_t>(v) << 11) |
                                     (static_cast<std::uint64_t>(w) << 22);
          records.push_back({hash, code});
        }
      }
    }
    std::cerr << "valid_signed_triples=" << records.size() << "\n";
    std::sort(records.begin(), records.end(), [](const Record& x, const Record& y) {
      if (x.hash != y.hash) return x.hash < y.hash;
      return x.code < y.code;
    });

    std::uint64_t hash_groups_with_repetition = 0;
    std::uint64_t exact_signature_groups_with_repetition = 0;
    std::uint64_t exact_representation_pairings = 0;
    std::uint64_t cross_compatible_pairings = 0;
    std::uint64_t fully_compatible = 0;
    std::array<int, 7> first_solution{};
    bool have_solution = false;

    std::size_t hash_begin = 0;
    while (hash_begin < records.size()) {
      std::size_t hash_end = hash_begin + 1;
      while (hash_end < records.size() &&
             records[hash_end].hash == records[hash_begin].hash) {
        ++hash_end;
      }
      if (hash_end - hash_begin >= 2) {
        ++hash_groups_with_repetition;
        std::vector<FullRecord> full;
        full.reserve(hash_end - hash_begin);
        for (std::size_t i = hash_begin; i < hash_end; ++i) {
          const auto triple = unpack(records[i].code);
          const auto key = signature(triple, positive_masks);
          full.push_back({key.first, key.second, records[i].code});
        }
        std::sort(full.begin(), full.end(), [](const FullRecord& x,
                                               const FullRecord& y) {
          if (x.parity != y.parity) return x.parity < y.parity;
          if (x.majority != y.majority) return x.majority < y.majority;
          return x.code < y.code;
        });
        std::size_t exact_begin = 0;
        while (exact_begin < full.size()) {
          std::size_t exact_end = exact_begin + 1;
          while (exact_end < full.size() &&
                 full[exact_end].parity == full[exact_begin].parity &&
                 full[exact_end].majority == full[exact_begin].majority) {
            ++exact_end;
          }
          if (exact_end - exact_begin >= 2) {
            ++exact_signature_groups_with_repetition;
            for (std::size_t x = exact_begin; x < exact_end; ++x) {
              const auto first = unpack(full[x].code);
              for (std::size_t y = x + 1; y < exact_end; ++y) {
                ++exact_representation_pairings;
                const auto second = unpack(full[y].code);
                if (!cross_compatible(first, second, coordinate, conflict)) continue;
                ++cross_compatible_pairings;
                if (!all_face_conditions(first, second, coordinate, literal_sign,
                                         face_sign)) {
                  continue;
                }
                ++fully_compatible;
                if (!have_solution) {
                  have_solution = true;
                  first_solution[0] = 0;
                  for (int t = 0; t < 3; ++t) {
                    first_solution[1 + t] = first[t];
                    first_solution[4 + t] = second[t] ^ 1;
                  }
                }
              }
            }
          }
          exact_begin = exact_end;
        }
      }
      hash_begin = hash_end;
    }

    std::cout << "{\n"
              << "  \"status\": \"EXACT_SEVEN_MITM_COMPLETE\",\n"
              << "  \"valid_signed_triples\": " << records.size() << ",\n"
              << "  \"hash_groups_with_repetition\": "
              << hash_groups_with_repetition << ",\n"
              << "  \"exact_signature_groups_with_repetition\": "
              << exact_signature_groups_with_repetition << ",\n"
              << "  \"exact_representation_pairings\": "
              << exact_representation_pairings << ",\n"
              << "  \"cross_compatible_pairings\": "
              << cross_compatible_pairings << ",\n"
              << "  \"fully_compatible_seven_term_vectors\": "
              << fully_compatible;
    if (have_solution) {
      std::cout << ",\n  \"first_solution_literal_ids\": [";
      for (int i = 0; i < 7; ++i) {
        if (i) std::cout << ", ";
        std::cout << first_solution[i];
      }
      std::cout << "]\n";
    } else {
      std::cout << "\n";
    }
    std::cout << "}\n";
    return 0;
  } catch (const std::exception& error) {
    std::cerr << "ERROR: " << error.what() << "\n";
    return 1;
  }
}
