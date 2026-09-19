// Blind re-derivation for pursekeeper/claims claim 2:
//   b(n) = number of permutations p of {1..n} that are derangements (p(i) != i for all i)
//          and avoid the classical pattern 4321 (no i<j<k<l with p(i)>p(j)>p(k)>p(l)).
//
// Written from the claim statement alone; the claimant's code was not consulted.
// Method: exhaustive enumeration with exact pruning on the longest decreasing
// subsequence ending at each new position. Nothing is printed from a table of
// answers: every term is computed here, and the program also prints the
// unconstrained 4321-avoider counts (A005802) as an independent cross-check of
// the enumerator itself.
//
// Build/run: see run.sh

#include <cstdio>
#include <cstdint>
#include <cstdlib>

static int N;
static int perm[64];   // perm[pos] = value placed at position pos (both 0-based)
static int lds_end[64]; // longest decreasing subsequence ending at position pos
static bool used[64];
static uint64_t count;

// Generic enumerator. When derangement_only is true, values equal to their
// position are rejected; either way any prefix that already contains a
// decreasing subsequence of length 4 is abandoned, because extending a prefix
// cannot remove one.
static void rec(int pos, bool derangement_only) {
    if (pos == N) { count++; return; }
    for (int v = 0; v < N; v++) {
        if (used[v]) continue;
        if (derangement_only && v == pos) continue;
        int L = 1;
        for (int i = 0; i < pos; i++)
            if (perm[i] > v && lds_end[i] + 1 > L) L = lds_end[i] + 1;
        if (L >= 4) continue;               // 4321 pattern would appear
        perm[pos] = v; lds_end[pos] = L; used[v] = true;
        rec(pos + 1, derangement_only);
        used[v] = false;
    }
}

static uint64_t count_for(int n, bool derangement_only) {
    N = n; count = 0;
    for (int i = 0; i < 64; i++) { perm[i] = -1; lds_end[i] = 0; used[i] = false; }
    rec(0, derangement_only);
    return count;
}

int main(int argc, char **argv) {
    // The pass criterion's minimum is b(1..12); the claim also states b(13..24).
    // NMAX selects how far to go: default 12 (the minimum, ~22 s), 13 to check
    // the claim's own next term, which is the strongest possible falsifier.
    int NMAX = (argc > 1) ? atoi(argv[1]) : 12;
    if (NMAX < 1 || NMAX > 20) NMAX = 12;

    // Independent cross-check of the enumerator: with the derangement condition
    // removed the same code must reproduce A005802 (4321-avoiders), whose terms
    // are known independently of this claim.
    static const uint64_t A005802[14] =
        {0, 1, 2, 6, 23, 103, 513, 2761, 15767, 94359, 586590, 3763290, 24792705,
         167078577};   // values read from https://oeis.org/A005802/b005802.txt, not from memory

    printf("cross-check: unconstrained 4321-avoiders (A005802)\n");
    int ok = 1;
    for (int n = 1; n <= NMAX; n++) {
        uint64_t got = count_for(n, false);
        printf("  n=%2d got=%11llu expected=%11llu %s\n", n,
               (unsigned long long)got, (unsigned long long)A005802[n],
               got == A005802[n] ? "OK" : "MISMATCH");
        fflush(stdout);
        if (got != A005802[n]) ok = 0;
    }
    printf("cross-check %s\n\n", ok ? "PASSED" : "FAILED");

    printf("b(n) = derangements avoiding 4321\n");
    for (int n = 1; n <= NMAX; n++) {
        printf("  b(%2d) = %llu\n", n, (unsigned long long)count_for(n, true));
        fflush(stdout);
    }

    printf("\nb(1..%d) = ", NMAX);
    for (int n = 1; n <= NMAX; n++)
        printf("%s%llu", n == 1 ? "" : ", ", (unsigned long long)count_for(n, true));
    printf("\n");
    return ok ? 0 : 1;
}
