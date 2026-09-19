// Blind re-derivation for pursekeeper/claims claims 11 and 12.
//
// Claim 11 (spanning-tree statistics of free polyominoes):
//   tau(P)  = number of spanning trees of the cell graph
//   M(n)    = max tau over free n-cell polyominoes
//   NM(n)   = how many attain it
//   SUM(n)  = sum of tau
//   DIST(n) = number of distinct tau values
//   UNI(n)  = number of free n-cell polyominoes whose cell graph has n edges
// Claim 12 (independent-set and domino-tiling statistics):
//   i(P) = number of independent sets, m(P) = number of perfect matchings
//   IMIN, IMAX, ISUM, IDIST over free n-cell polyominoes
//   MSUM(k), MMAX(k) over free 2k-cell polyominoes
//
// Written from the claim statements alone; the claimant's code was not consulted.
// Nothing is printed from a table of answers: every value is computed here.
// `run.sh` prints the minimum ranges (n <= 13, k <= 6); pass a larger NMAX for more.
//
// Independent cross-checks built into the run:
//   * free polyomino counts must reproduce OEIS A000105 (1,1,1,2,5,12,35,108,...)
//   * tau of the 3x3 square must be 192 (a value known independently of the claim)
//   * i of the 2x2 square must be 7, i of the straight tetromino (P4) must be 8

#include <cstdio>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <set>
#include <vector>
#include <array>
#include <algorithm>

typedef std::vector<std::pair<int,int>> Shape;

// ---------- canonical form under the 8 symmetries of the square ----------
static Shape canon(const Shape &s) {
    Shape best;
    bool first = true;
    for (int t = 0; t < 8; t++) {
        Shape q;
        q.reserve(s.size());
        for (size_t i = 0; i < s.size(); i++) {
            int x = s[i].first, y = s[i].second;
            if (t & 4) { int tmp = x; x = y; y = tmp; }   // transpose
            if (t & 1) x = -x;                             // reflect
            if (t & 2) y = -y;
            q.push_back({x, y});
        }
        int mx = q[0].first, my = q[0].second;
        for (size_t i = 1; i < q.size(); i++) {
            mx = std::min(mx, q[i].first);
            my = std::min(my, q[i].second);
        }
        for (size_t i = 0; i < q.size(); i++) { q[i].first -= mx; q[i].second -= my; }
        std::sort(q.begin(), q.end());
        if (first || q < best) { best = q; first = false; }
    }
    return best;
}

// ---------- all free polyominoes with exactly n cells ----------
static std::vector<Shape> free_polyominoes(int n) {
    std::set<Shape> cur;
    cur.insert(Shape{{0, 0}});
    for (int size = 1; size < n; size++) {
        std::set<Shape> next;
        for (const Shape &s : cur) {
            std::set<std::pair<int,int>> occ(s.begin(), s.end());
            for (const std::pair<int,int> &c : s) {
                static const int dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, 1, -1};
                for (int d = 0; d < 4; d++) {
                    std::pair<int,int> q{c.first + dx[d], c.second + dy[d]};
                    if (occ.count(q)) continue;
                    Shape ext = s;
                    ext.push_back(q);
                    next.insert(canon(ext));
                }
            }
        }
        cur.swap(next);
    }
    return std::vector<Shape>(cur.begin(), cur.end());
}

// ---------- exact integer determinant by Bareiss' fraction-free algorithm ----------
static long long det_bareiss(std::vector<std::vector<long long>> a) {
    int n = (int)a.size();
    if (n == 0) return 1;
    long long prev = 1, sign = 1;
    for (int k = 0; k + 1 < n; k++) {
        if (a[k][k] == 0) {
            int piv = -1;
            for (int i = k + 1; i < n; i++) if (a[i][k] != 0) { piv = i; break; }
            if (piv < 0) return 0;
            std::swap(a[k], a[piv]);
            sign = -sign;
        }
        for (int i = k + 1; i < n; i++)
            for (int j = k + 1; j < n; j++)
                a[i][j] = (a[i][j] * a[k][k] - a[i][k] * a[k][j]) / prev;
        prev = a[k][k];
    }
    return sign * a[n - 1][n - 1];
}

// ---------- per-shape statistics ----------
struct Stats {
    long long tau;        // spanning trees (claim 11)
    long long ind;        // independent sets (claim 12)
    long long match;      // perfect matchings (claim 12)
    int       edges;      // edges of the cell graph (claim 11's UNI)
};

static Stats analyse(const Shape &s) {
    int n = (int)s.size();
    int adj[32][32];
    memset(adj, 0, sizeof adj);
    int edges = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) {
            int dx = std::abs(s[i].first - s[j].first);
            int dy = std::abs(s[i].second - s[j].second);
            if (dx + dy == 1) { adj[i][j] = adj[j][i] = 1; edges++; }
        }

    Stats st; st.edges = edges;

    // spanning trees: any cofactor of the Laplacian
    if (n == 1) {
        st.tau = 1;
    } else {
        std::vector<std::vector<long long>> L(n - 1, std::vector<long long>(n - 1, 0));
        for (int i = 0; i + 1 < n; i++)
            for (int j = 0; j + 1 < n; j++) {
                if (i == j) {
                    int deg = 0;
                    for (int k = 0; k < n; k++) deg += adj[i][k];
                    L[i][j] = deg;
                } else {
                    L[i][j] = -adj[i][j];
                }
            }
        st.tau = det_bareiss(L);
    }

    // independent sets and perfect matchings by bitmask DP (n <= 32 here, n <= 24 practical)
    // independent sets: count subsets with no adjacent pair
    long long ind = 0;
    uint32_t nbr[32];
    for (int i = 0; i < n; i++) {
        uint32_t m = 0;
        for (int j = 0; j < n; j++) if (adj[i][j]) m |= (1u << j);
        nbr[i] = m;
    }
    std::vector<char> is_ind(1u << n, 0);
    for (uint32_t S = 0; S < (1u << n); S++) {
        int low = -1;
        for (int i = 0; i < n; i++) if (S & (1u << i)) { low = i; break; }
        if (low < 0) { is_ind[S] = 1; ind++; continue; }
        uint32_t rest = S & ~(1u << low);
        is_ind[S] = (is_ind[rest] && ((nbr[low] & rest) == 0)) ? 1 : 0;
        ind += is_ind[S];
    }
    st.ind = ind;

    // perfect matchings: DP over covered-cell masks
    std::vector<long long> dp(1u << n, 0);
    dp[0] = 1;
    long long match = 0;
    for (uint32_t S = 0; S < (1u << n); S++) {
        if (!dp[S]) continue;
        int low = -1;
        for (int i = 0; i < n; i++) if (!(S & (1u << i))) { low = i; break; }
        if (low < 0) { match += dp[S]; continue; }
        for (int j = low + 1; j < n; j++)
            if (!(S & (1u << j)) && adj[low][j]) dp[S | (1u << low) | (1u << j)] += dp[S];
    }
    st.match = match;
    return st;
}

// square grid graph m x m -> tau, used for the independent cross-check
static long long tau_grid(int m) {
    Shape s;
    for (int i = 0; i < m; i++) for (int j = 0; j < m; j++) s.push_back({i, j});
    return analyse(s).tau;
}
static long long ind_grid(int m) { return 0; }

int main(int argc, char **argv) {
    int NMAX = (argc > 1) ? atoi(argv[1]) : 13;
    if (NMAX < 1 || NMAX > 16) NMAX = 13;

    // ---- cross-checks on values known independently of the claim ----
    // values from https://oeis.org/A000105/b000105.txt, not from memory
    static const long long A000105[17] =
        {1, 1, 1, 2, 5, 12, 35, 108, 369, 1285, 4655, 17073, 63600, 238591,
         901971, 3426576, 13079255};
    printf("cross-check 1: free polyomino counts vs OEIS A000105\n");
    int ok = 1;
    for (int n = 1; n <= NMAX; n++) {
        long long got = (long long)free_polyominoes(n).size();
        if (got != A000105[n]) ok = 0;
        printf("  n=%2d got=%8lld expected=%8lld %s\n", n, got, A000105[n],
               got == A000105[n] ? "OK" : "MISMATCH");
    }
    printf("cross-check 1 %s\n\n", ok ? "PASSED" : "FAILED");
    if (!ok) { printf("enumerator is wrong - stopping\n"); return 1; }

    printf("cross-check 2: tau of the 3x3 square must be 192 (known independently)\n");
    long long t33 = tau_grid(3);
    printf("  tau(3x3) = %lld %s\n\n", t33, t33 == 192 ? "OK" : "MISMATCH");
    if (t33 != 192) { printf("spanning-tree routine is wrong - stopping\n"); return 1; }

    printf("cross-check 3: independent sets of P4 (straight tetromino) must be 8\n");
    Shape p4{{0, 0}, {1, 0}, {2, 0}, {3, 0}};
    long long i_p4 = analyse(p4).ind;
    printf("  i(P4) = %lld, i(2x2 square) = %lld (expected 8 and 7)\n\n",
           i_p4, analyse(Shape{{0,0},{1,0},{0,1},{1,1}}).ind);
    if (i_p4 != 8) { printf("independent-set routine is wrong - stopping\n"); return 1; }

    // ---- claim 11 sequences ----
    printf("claim 11: spanning-tree statistics of free polyominoes (n = 1..%d)\n", NMAX);
    std::vector<long long> M(NMAX + 1), NM(NMAX + 1), SUM(NMAX + 1), DIST(NMAX + 1), UNI(NMAX + 1);
    std::vector<long long> IMIN(NMAX + 1), IMAX(NMAX + 1), ISUM(NMAX + 1), IDIST(NMAX + 1);
    std::set<std::pair<int,long long>> tau1;   // (n, ) for the A131482 side condition
    std::vector<long long> TAU1(NMAX + 1, 0);

    for (int n = 1; n <= NMAX; n++) {
        std::vector<Shape> all = free_polyominoes(n);
        long long mx = -1, sum = 0, nmx = 0, uni = 0, cnt1 = 0;
        long long imin = -1, imax = -1, isum = 0;
        std::set<long long> dist, idist;
        for (const Shape &s : all) {
            Stats st = analyse(s);
            if (st.tau > mx) { mx = st.tau; nmx = 1; } else if (st.tau == mx) nmx++;
            sum += st.tau;
            dist.insert(st.tau);
            if (st.edges == n) uni++;
            if (st.tau == 1) cnt1++;

            if (imin < 0 || st.ind < imin) imin = st.ind;
            if (st.ind > imax) imax = st.ind;
            isum += st.ind;
            idist.insert(st.ind);
        }
        M[n] = mx; NM[n] = nmx; SUM[n] = sum; DIST[n] = (long long)dist.size(); UNI[n] = uni;
        IMIN[n] = imin; IMAX[n] = imax; ISUM[n] = isum; IDIST[n] = (long long)idist.size();
        TAU1[n] = cnt1;
    }

    printf("  M(1..%d)    = ", NMAX);
    for (int n = 1; n <= NMAX; n++) printf("%s%lld", n == 1 ? "" : ", ", M[n]);
    printf("\n  NM(1..%d)   = ", NMAX);
    for (int n = 1; n <= NMAX; n++) printf("%s%lld", n == 1 ? "" : ", ", NM[n]);
    printf("\n  SUM(1..%d)  = ", NMAX);
    for (int n = 1; n <= NMAX; n++) printf("%s%lld", n == 1 ? "" : ", ", SUM[n]);
    printf("\n  DIST(1..%d) = ", NMAX);
    for (int n = 1; n <= NMAX; n++) printf("%s%lld", n == 1 ? "" : ", ", DIST[n]);
    printf("\n  UNI(1..%d)  = ", NMAX);
    for (int n = 1; n <= NMAX; n++) printf("%s%lld", n == 1 ? "" : ", ", UNI[n]);
    printf("\n  side condition, polyominoes with tau = 1 (A131482), n = 1..%d =\n    ", NMAX);
    for (int n = 1; n <= NMAX; n++) printf("%s%lld", n == 1 ? "" : ", ", TAU1[n]);
    printf("\n\n");

    // ---- claim 12 sequences ----
    printf("claim 12: independent-set and domino-tiling statistics (n = 1..%d)\n", NMAX);
    printf("  IMIN(1..%d)  = ", NMAX);
    for (int n = 1; n <= NMAX; n++) printf("%s%lld", n == 1 ? "" : ", ", IMIN[n]);
    printf("\n  IMAX(1..%d)  = ", NMAX);
    for (int n = 1; n <= NMAX; n++) printf("%s%lld", n == 1 ? "" : ", ", IMAX[n]);
    printf("\n  ISUM(1..%d)  = ", NMAX);
    for (int n = 1; n <= NMAX; n++) printf("%s%lld", n == 1 ? "" : ", ", ISUM[n]);
    printf("\n  IDIST(1..%d) = ", NMAX);
    for (int n = 1; n <= NMAX; n++) printf("%s%lld", n == 1 ? "" : ", ", IDIST[n]);

    printf("\n  MSUM(k) and MMAX(k) over free 2k-cell polyominoes, k = 1..%d\n", NMAX / 2);
    printf("  MSUM = ");
    for (int k = 1; k <= NMAX / 2; k++) {
        long long sum = 0, mx = -1;
        for (const Shape &s : free_polyominoes(2 * k)) {
            Stats st = analyse(s);
            sum += st.match;
            if (st.match > mx) mx = st.match;
        }
        printf("%s%lld", k == 1 ? "" : ", ", sum);
    }
    printf("\n  MMAX = ");
    for (int k = 1; k <= NMAX / 2; k++) {
        long long mx = -1;
        for (const Shape &s : free_polyominoes(2 * k)) {
            Stats st = analyse(s);
            if (st.match > mx) mx = st.match;
        }
        printf("%s%lld", k == 1 ? "" : ", ", mx);
    }
    printf("\n");
    return 0;
}
