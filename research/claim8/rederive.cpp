// Blind re-derivation of pursekeeper claim 8:
// "Geometrically distinct knight's tours on polyomino boards".
//
// Everything here is computed from the statement alone: free n-cell polyominoes
// (holes allowed), the induced knight graph, Hamiltonian paths/cycles, the board's
// automorphism group as cell permutations, orbits and symmetric orbits.
//
// No answer literals: this program computes and prints only.
//
// usage: rederive [max_n]      (default: 12, the claim's stated minimum)
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long u64;
typedef __uint128_t u128;

static int TargetN;
static int W, OFF;
static vector<unsigned char> grid;
struct Pt { int x, y; };

// canonical free form of a cell set under the 8 symmetries of the square lattice,
// as a 128-bit key packed 8 bits per cell (used both for dedup and for decoding).
static u128 freeKeyBits(const vector<Pt>& cells) {
    u128 best = ~(u128)0;
    for (int t = 0; t < 8; ++t) {
        vector<Pt> v; v.reserve(cells.size());
        for (const auto& p : cells) {
            int x = p.x, y = p.y;
            if (t & 1) { int tmp = x; x = y; y = tmp; }
            if (t & 2) x = -x;
            if (t & 4) y = -y;
            v.push_back({x, y});
        }
        int mx = INT_MAX, my = INT_MAX;
        for (auto& p : v) { mx = min(mx, p.x); my = min(my, p.y); }
        for (auto& p : v) { p.x -= mx; p.y -= my; }
        sort(v.begin(), v.end(), [](const Pt& a, const Pt& b) {
            return a.x != b.x ? a.x < b.x : a.y < b.y;
        });
        u128 key = 0;
        for (auto& p : v) key = (key << 8) | (u128)((p.x << 4) | p.y);
        best = min(best, key);
    }
    return best;
}

static vector<Pt> cur;
struct U128Hash { size_t operator()(u128 x) const { return (size_t)(x ^ (x >> 64)); } };
static unordered_set<u128, U128Hash> freeSet;

// Redelmeier enumeration of fixed polyominoes, deduped to free form by freeKey.
static void rec(int n, Pt added, vector<Pt> untried) {
    cur.push_back(added);
    if (n == TargetN) {
        freeSet.insert(freeKeyBits(cur));
        cur.pop_back();
        return;
    }
    static const int dx[4] = {1, -1, 0, 0};
    static const int dy[4] = {0, 0, 1, -1};
    for (int d = 0; d < 4; ++d) {
        int nx = added.x + dx[d], ny = added.y + dy[d];
        if (!grid[(nx + OFF) * W + (ny + OFF)]) {
            bool found = false;
            for (auto& p : untried) if (p.x == nx && p.y == ny) { found = true; break; }
            if (!found) untried.push_back({nx, ny});
        }
    }
    for (size_t i = 0; i < untried.size(); ++i) {
        Pt p = untried[i];
        vector<Pt> sub(untried.begin() + i + 1, untried.end());
        grid[(p.x + OFF) * W + (p.y + OFF)] = 1;
        rec(n + 1, p, sub);
        grid[(p.x + OFF) * W + (p.y + OFF)] = 0;
    }
    cur.pop_back();
}

static vector<Pt> decode(u128 key, int n) {
    vector<Pt> v;
    for (int i = 0; i < n; ++i) {
        unsigned char b = (unsigned char)((key >> (8 * i)) & 0xFF);
        v.push_back({b >> 4, b & 15});
    }
    sort(v.begin(), v.end(), [](const Pt& a, const Pt& b) {
        return a.x != b.x ? a.x < b.x : a.y < b.y;
    });
    return v;
}

// automorphisms of the board: the D4 elements that map the cell set onto itself
static vector<vector<int>> automorphisms(const vector<Pt>& cells) {
    int n = cells.size();
    map<pair<int, int>, int> idx;
    for (int i = 0; i < n; ++i) idx[{cells[i].x, cells[i].y}] = i;
    vector<vector<int>> res;
    for (int t = 0; t < 8; ++t) {
        vector<Pt> img(n);
        for (int i = 0; i < n; ++i) {
            int x = cells[i].x, y = cells[i].y;
            if (t & 1) { int tmp = x; x = y; y = tmp; }
            if (t & 2) x = -x;
            if (t & 4) y = -y;
            img[i] = {x, y};
        }
        int mx = INT_MAX, my = INT_MAX;
        for (auto& p : img) { mx = min(mx, p.x); my = min(my, p.y); }
        for (auto& p : img) { p.x -= mx; p.y -= my; }
        bool ok = true;
        vector<int> perm(n, -1);
        for (int i = 0; i < n; ++i) {
            auto it = idx.find({img[i].x, img[i].y});
            if (it == idx.end()) { ok = false; break; }
            perm[i] = it->second;
        }
        if (ok) res.push_back(perm);
    }
    return res;
}

static string canonPath(const vector<int>& s) {
    vector<int> r(s.rbegin(), s.rend());
    const vector<int>& b = (r < s) ? r : s;
    string out;
    for (int x : b) { out += to_string(x); out += ','; }
    return out;
}

static string canonCycle(const vector<int>& s) {
    int n = s.size();
    int m = 0;
    for (int i = 1; i < n; ++i) if (s[i] < s[m]) m = i;
    vector<int> f(n), g(n);
    for (int i = 0; i < n; ++i) { f[i] = s[(m + i) % n]; g[i] = s[(m - i + n) % n]; }
    const vector<int>& b = (g < f) ? g : f;
    string out;
    for (int x : b) { out += to_string(x); out += ','; }
    return out;
}

// orbit of an undirected tour under Aut(B): distinct images, plus the orbit's
// canonical representative (min over the group) and whether the orbit is symmetric.
static bool orbitOf(const vector<int>& seq, const vector<vector<int>>& aut,
                    bool cycle, string& repOut, int& sizeOut) {
    vector<string> imgs;
    for (const auto& g : aut) {
        vector<int> s(seq.size());
        for (size_t i = 0; i < seq.size(); ++i) s[i] = g[seq[i]];
        string c = cycle ? canonCycle(s) : canonPath(s);
        bool dup = false;
        for (auto& e : imgs) if (e == c) { dup = true; break; }
        if (!dup) imgs.push_back(c);
    }
    sizeOut = imgs.size();
    string best = imgs[0];
    for (auto& e : imgs) if (e < best) best = e;
    repOut = best;
    return sizeOut < (int)aut.size();
}

struct BoardCounts {
    long long Ropen = 0, Rclosed = 0, Topen = 0, Tclosed = 0, Sopen = 0, Sclosed = 0;
};

static void analyze(const vector<Pt>& cells, BoardCounts& C) {
    int n = cells.size();
    // knight graph
    vector<vector<int>> adj(n);
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) {
            if (i == j) continue;
            int dx = abs(cells[i].x - cells[j].x), dy = abs(cells[i].y - cells[j].y);
            if ((dx == 1 && dy == 2) || (dx == 2 && dy == 1)) adj[i].push_back(j);
        }
    vector<vector<int>> aut = automorphisms(cells);

    unordered_set<string> seenOpen, seenClosed;
    vector<int> seq;
    vector<char> used(n, 0);

    // Hamiltonian paths: enumerate oriented, keep each undirected path once
    function<void(int)> dfsP = [&](int u) {
        seq.push_back(u);
        used[u] = 1;
        if ((int)seq.size() == n) {
            if (seq.front() < seq.back()) {
                C.Ropen++;
                string rep; int osz;
                bool sym = orbitOf(seq, aut, false, rep, osz);
                if (seenOpen.insert(rep).second) { C.Topen++; if (sym) C.Sopen++; }
            }
        } else {
            for (int v : adj[u]) if (!used[v]) dfsP(v);
        }
        used[u] = 0;
        seq.pop_back();
    };
    for (int s = 0; s < n; ++s) dfsP(s);

    // Hamiltonian cycles: fix start at cell 0, keep each undirected cycle once
    function<void(int)> dfsC = [&](int u) {
        seq.push_back(u);
        used[u] = 1;
        if ((int)seq.size() == n) {
            bool closed = false;
            for (int v : adj[u]) if (v == 0) { closed = true; break; }
            if (closed && seq.size() >= 3 && seq[1] < seq.back()) {
                C.Rclosed++;
                string rep; int osz;
                bool sym = orbitOf(seq, aut, true, rep, osz);
                if (seenClosed.insert(rep).second) { C.Tclosed++; if (sym) C.Sclosed++; }
            }
        } else {
            for (int v : adj[u]) if (!used[v]) dfsC(v);
        }
        used[u] = 0;
        seq.pop_back();
    };
    if (n >= 3) dfsC(0);
}

int main(int argc, char** argv) {
    int maxN = (argc > 1) ? atoi(argv[1]) : 12;
    vector<long long> Ropen(maxN + 1), Rclosed(maxN + 1), Topen(maxN + 1),
        Tclosed(maxN + 1), Sopen(maxN + 1), Sclosed(maxN + 1);
    vector<long long> freeCount(maxN + 1), fixedCount(maxN + 1);

    for (int n = 1; n <= maxN; ++n) {
        TargetN = n; W = 2 * n + 3; OFF = n + 1;
        grid.assign(W * W, 0);
        freeSet.clear(); cur.clear();
        grid[(0 + OFF) * W + (0 + OFF)] = 1;
        rec(1, {0, 0}, {});
        freeCount[n] = freeSet.size();

        BoardCounts C;
        for (u128 key : freeSet) {
            vector<Pt> cells = decode(key, n);
            analyze(cells, C);
        }
        Ropen[n] = C.Ropen; Rclosed[n] = C.Rclosed;
        Topen[n] = C.Topen; Tclosed[n] = C.Tclosed;
        Sopen[n] = C.Sopen; Sclosed[n] = C.Sclosed;
    }

    auto pr = [&](const char* name, const vector<long long>& v, int lo, int hi) {
        printf("%s(%d..%d) = ", name, lo, hi);
        for (int n = lo; n <= hi; ++n) printf("%lld%s", v[n], n == hi ? "\n" : ", ");
    };
    int lo = 7;
    printf("free polyomino counts (n=%d..%d) = ", 1, maxN);
    for (int n = 1; n <= maxN; ++n) printf("%lld%s", freeCount[n], n == maxN ? "\n" : ", ");
    pr("T_open", Topen, lo, maxN);
    pr("T_closed", Tclosed, lo, maxN);
    pr("S_open", Sopen, lo, maxN);
    pr("S_closed", Sclosed, lo, maxN);
    pr("R_open", Ropen, lo, maxN);
    pr("R_closed", Rclosed, lo, maxN);
    return 0;
}
