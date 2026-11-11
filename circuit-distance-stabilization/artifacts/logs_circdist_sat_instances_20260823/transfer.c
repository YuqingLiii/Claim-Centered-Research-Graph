/* transfer.c -- min-plus transfer engine for d_R^sector(M).
 *
 * Reads a spec produced by run_transfer.py:
 *    dim nB Rmax cap ngen
 *    ngen lines:  key flag        (key = (class(E) << nB) | u(S), flag in {0,1})
 *    2^dim ints:  HZ[sigma]       (syndrome of the canonical representative)
 *
 * Stage 1 (dictionary): BFS on the Cayley graph of (Sigma x F2^B, XOR) with the
 * generator keys, carrying a monotone OR flag bit; W[state | flag<<(dim+nB)] is
 * the minimum number of elementary faults of a one-round multiset realising that
 * (residual class, record-flip) pair, using >=1 flagged fault when flag = 1.
 * By Lemma 2.9 (collision merging) this equals the minimum over configurations
 * for flag = 0 and lower-bounds it for flag = 1, which is the direction needed
 * for exclusion claims.
 *
 * Stage 2 (DP): layered min-plus product with the two boundary vectors, tracking
 * (flag_used, #rounds carrying faults capped at 2).  Values above `cap` are
 * reported as INF (they can never be the answer because d_R <= d <= cap).
 *
 * Output lines: "R <R> <variant> <value>"  with variants
 *    all        unrestricted d_R
 *    flag1      minimum over configurations using >=1 flagged fault
 *    flag0      minimum over configurations using no flagged fault
 *    rounds1    minimum over configurations whose faults sit in ONE round
 *    rounds2    minimum over configurations whose faults sit in >=2 rounds
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INF 63

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: transfer spec\n"); return 1; }
    FILE *f = fopen(argv[1], "r");
    if (!f) { perror("open"); return 1; }
    int dim, nB, Rmax, cap, ngen;
    if (fscanf(f, "%d %d %d %d %d", &dim, &nB, &Rmax, &cap, &ngen) != 5) return 1;
    unsigned int *gk = malloc(ngen * sizeof(unsigned int));
    int *gf = malloc(ngen * sizeof(int));
    for (int i = 0; i < ngen; i++) if (fscanf(f, "%u %d", &gk[i], &gf[i]) != 2) return 1;
    long N = 1L << dim, SZ = 1L << (dim + nB);
    unsigned int *HZ = malloc(N * sizeof(unsigned int));
    for (long i = 0; i < N; i++) if (fscanf(f, "%u", &HZ[i]) != 1) return 1;
    fclose(f);

    unsigned char *W = malloc(2 * SZ);
    memset(W, INF, 2 * SZ);
    W[0] = 0;
    unsigned int *cur = malloc((size_t)(2 * SZ) * sizeof(unsigned int));
    unsigned int *nxt = malloc((size_t)(2 * SZ) * sizeof(unsigned int));
    long ncur = 1, nnxt;
    cur[0] = 0;
    for (int lvl = 0; lvl < cap && ncur > 0; lvl++) {
        nnxt = 0;
        for (long i = 0; i < ncur; i++) {
            unsigned int s = cur[i];
            unsigned int base = s & (unsigned int)(SZ - 1);
            unsigned int fl = s >> (dim + nB);
            for (int g = 0; g < ngen; g++) {
                unsigned int t = (base ^ gk[g]) | ((fl | (unsigned int)gf[g]) << (dim + nB));
                if (W[t] == INF) { W[t] = (unsigned char)(lvl + 1); nxt[nnxt++] = t; }
            }
        }
        unsigned int *tmp = cur; cur = nxt; nxt = tmp; ncur = nnxt;
        fprintf(stderr, "  bfs level %d : %ld new states\n", lvl + 1, ncur);
    }
    free(cur); free(nxt);

    /* layered DP.  layer = flag*3 + rounds_used(capped 2) */
    const int NL = 6;
    unsigned char *ALL = malloc((size_t)NL * N * (Rmax + 1));
    memset(ALL, INF, (size_t)NL * N * (Rmax + 1));
    unsigned char *fv = ALL, *gv;
    fv[0 * N + 0] = 0;
    for (int R = 1; R <= Rmax; R++) {
        fv = ALL + (size_t)(R - 1) * NL * N;
        gv = ALL + (size_t)R * NL * N;
        for (int l = 0; l < NL; l++) {
            int fl = l / 3, rc = l % 3;
            unsigned char *row = fv + (long)l * N;
            for (long s = 0; s < N; s++) {
                int c = row[s];
                if (c > cap) continue;
                long base = (s << nB) | HZ[s];
                for (long sp = 0; sp < N; sp++) {
                    long idx = base ^ (sp << nB);
                    int w0 = W[idx], w1 = W[idx + SZ];
                    if (w0 <= cap - c) {
                        int nrc = rc + (w0 > 0 ? 1 : 0); if (nrc > 2) nrc = 2;
                        int nl = fl * 3 + nrc;
                        if (c + w0 < gv[(long)nl * N + sp]) gv[(long)nl * N + sp] = (unsigned char)(c + w0);
                    }
                    if (w1 <= cap - c) {
                        int nrc = rc + (w1 > 0 ? 1 : 0); if (nrc > 2) nrc = 2;
                        int nl = 1 * 3 + nrc;
                        if (c + w1 < gv[(long)nl * N + sp]) gv[(long)nl * N + sp] = (unsigned char)(c + w1);
                    }
                }
            }
        }
        int best[5]; for (int i = 0; i < 5; i++) best[i] = INF;
        int bl = -1; long bs = -1;
        for (int l = 0; l < NL; l++) {
            int fl = l / 3, rc = l % 3;
            for (long s = 1; s < N; s++) {
                if (HZ[s] != 0) continue;
                int c = gv[(long)l * N + s];
                if (c > cap) continue;
                if (c < best[0]) { best[0] = c; bl = l; bs = s; }
                if (fl == 1 && c < best[1]) best[1] = c;
                if (fl == 0 && c < best[2]) best[2] = c;
                if (rc <= 1 && c < best[3]) best[3] = c;
                if (rc >= 2 && c < best[4]) best[4] = c;
            }
        }
        const char *nm[5] = {"all", "flag1", "flag0", "rounds1", "rounds2"};
        for (int i = 0; i < 5; i++) printf("R %d %s %d\n", R, nm[i], best[i]);
        /* backtrack an optimal path for the unrestricted variant */
        if (bs >= 0) {
            long *ps = malloc((R + 1) * sizeof(long));
            int *pw = malloc((R + 1) * sizeof(int));
            long s = bs; int l = bl, c = best[0], ok = 1;
            ps[R] = s;
            for (int r = R; r >= 1; r--) {
                unsigned char *pv = ALL + (size_t)(r - 1) * NL * N;
                int found = 0;
                for (int lp = 0; lp < NL && !found; lp++) {
                    for (long sp = 0; sp < N; sp++) {
                        int cp = pv[(long)lp * N + sp];
                        if (cp > cap) continue;
                        long idx = ((sp << nB) | HZ[sp]) ^ (s << nB);
                        int w0 = W[idx], w1 = W[idx + SZ];
                        int fl = lp / 3, rc = lp % 3;
                        for (int which = 0; which < 2; which++) {
                            int w = which ? w1 : w0;
                            if (w > cap || cp + w != c) continue;
                            int nrc = rc + (w > 0 ? 1 : 0); if (nrc > 2) nrc = 2;
                            int nl = (which ? 1 : fl) * 3 + nrc;
                            if (nl != l) continue;
                            ps[r - 1] = sp; pw[r] = w; s = sp; l = lp; c = cp; found = 1; break;
                        }
                        if (found) break;
                    }
                }
                if (!found) { ok = 0; break; }
            }
            if (ok && ps[0] == 0) {
                printf("PATH %d", R);
                for (int r = 0; r <= R; r++) printf(" %ld", ps[r]);
                printf(" |");
                for (int r = 1; r <= R; r++) printf(" %d", pw[r]);
                printf("\n");
            }
            free(ps); free(pw);
        }
        fflush(stdout);
    }
    return 0;
}
