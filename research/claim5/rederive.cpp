/* Claim 5 blind re-derivation: OEIS A396786 three further terms
 * 
 * Author: Rai, an autonomous AI agent (Hermes Agent; DeepSeek-family model).
 * Blind re-derivation from the claim statement alone, without seeing the
 * claimant's code.
 *
 * a(n) = smallest prime p such that for every prime q among the first n primes,
 *        p^(q^3) ≡ 1 (mod q^5) or p^(q^3) ≡ -1 (mod q^5)
 *
 * The claim covers n = 1..11. Published a(1..8) are used as offline validation
 * only; no answer literals appear in this source.
 *
 * Method: for each n, enumerate the 2^(#odd q) CRT residue classes where
 * p ≡ ±1 (mod q^2) for each odd q ≤ the n-th prime. Scan each class for the
 * smallest prime, then verify with the direct q^5 exponentiation.
 * 
 * Output: a(9) = <computed value>    (minimum pass criterion)
 */

#include <iostream>
#include <cstdint>
#include <cassert>
#include <vector>
#include <algorithm>

using u64 = uint64_t;
using u128 = __uint128_t;

// -------------------------------------------------------------------------
// 64-bit deterministic Miller-Rabin (Jaeschke / Sinclair bases)
// -------------------------------------------------------------------------
static bool is_prime(u64 n) {
    if (n < 2) return false;
    const u64 small[] = {2,3,5,7,11,13,17,19,23,29,31,37};
    for (u64 p : small) {
        if (n % p == 0) return n == p;
    }
    u64 d = n - 1; int s = 0;
    while ((d & 1) == 0) { d >>= 1; ++s; }
    const u64 bases[] = {2, 325, 9375, 28178, 450775, 9780504, 1795265022};
    for (u64 a : bases) {
        if (a % n == 0) continue;
        u64 x = 1; u128 base = a, exp = d, mod = n;
        for (base %= mod; exp; exp >>= 1) {
            if (exp & 1) x = (u128(x) * base) % mod;
            base = (base * base) % mod;
        }
        if (x == 1 || x == n-1) continue;
        bool composite = true;
        for (int r = 0; r < s-1; ++r) {
            x = (u128(x) * x) % mod;
            if (x == n-1) { composite = false; break; }
        }
        if (composite) return false;
    }
    return true;
}

// Next prime >= x (x >= 2)
static u64 next_prime(u64 x) {
    if (x <= 2) return 2;
    if (x % 2 == 0) ++x;
    while (!is_prime(x)) x += 2;
    return x;
}

// -------------------------------------------------------------------------
// Integer arithmetic helpers
// -------------------------------------------------------------------------
// pow_mod(a, e, m) with a < m, u128 intermediate
static u64 pow_mod(u64 a, u64 e, u64 m) {
    u64 r = 1;
    for (a %= m; e; e >>= 1) {
        if (e & 1) r = (u128(r) * a) % m;
        a = (u128(a) * a) % m;
    }
    return r;
}

// Extended GCD: returns (g, x, y) where g = gcd(a,b) = a*x + b*y
struct EGcd { u64 g; int64_t x, y; };
static EGcd egcd(int64_t a, int64_t b) {
    if (b == 0) return { (u64)std::abs(a), a >= 0 ? 1 : -1, 0 };
    auto [g, x1, y1] = egcd(b, a % b);
    return { g, y1, x1 - (a / b) * y1 };
}

// Chinese remainder: given residues r_i and pairwise coprime moduli m_i,
// find x ≡ r_i (mod m_i). Returns (x, M = product of m_i).
struct CrtRes { u64 x; u64 M; };
static CrtRes crt_pair(u64 r1, u64 m1, u64 r2, u64 m2) {
    auto [g, inv_m1, _] = egcd((int64_t)m1, (int64_t)m2);
    (void)g; assert(g == 1);
    // inv_m1 = modular inverse of m1 modulo m2
    int64_t inv = inv_m1 % (int64_t)m2;
    if (inv < 0) inv += m2;
    u64 M = m1 * m2;
    u64 x = (r1 + m1 * (( (int64_t(r2)-int64_t(r1)) % (int64_t)m2 + (int64_t)m2) % m2 * inv % m2)) % M;
    return { x, M };
}

static CrtRes crt(const std::vector<u64>& residues, const std::vector<u64>& moduli) {
    u64 r = 0, m = 1;
    for (size_t i = 0; i < residues.size(); ++i) {
        auto cr = crt_pair(r % m, m, residues[i] % moduli[i], moduli[i]);
        r = cr.x; m = cr.M;
    }
    return { r, m };
}

// -------------------------------------------------------------------------
// First N primes
// -------------------------------------------------------------------------
static std::vector<u64> first_primes(int n) {
    std::vector<u64> res;
    u64 p = 2;
    while ((int)res.size() < n) {
        res.push_back(p);
        p = next_prime(p + 1);
    }
    return res;
}

// -------------------------------------------------------------------------
// Direct check: p^(q^3) ≡ ±1 (mod q^5)
// -------------------------------------------------------------------------
static bool check_a_n(u64 p, const std::vector<u64>& qs) {
    for (u64 q : qs) {
        // q^3 and q^5: compute directly (q <= 31, so q^5 fits in 32-bit)
        u64 q3 = q * q * q;
        u64 q5 = q3 * q * q;
        u64 r = pow_mod(p, q3, q5);
        if (r != 1 && r != q5 - 1) return false;
    }
    return true;
}

// -------------------------------------------------------------------------
// Find a(n): the smallest prime satisfying the condition for first n primes
// -------------------------------------------------------------------------
static u64 find_a_n(int n) {
    auto qs = first_primes(n);
    std::vector<u64> odd_q;
    for (u64 q : qs) if (q != 2) odd_q.push_back(q);
    
    u64 best = ~0ULL;  // large sentinel
    
    // For each CRT sign combination
    int n_signs = (int)odd_q.size();
    for (int mask = 0; mask < (1 << n_signs); ++mask) {
        std::vector<u64> residues, moduli;
        for (int i = 0; i < n_signs; ++i) {
            int sign = (mask >> i) & 1 ? 1 : -1;
            u64 q2 = odd_q[i] * odd_q[i];
            residues.push_back(sign == 1 ? 1ULL : q2 - 1ULL);
            moduli.push_back(q2);
        }
        u64 r = 0, M = 1;
        if (!residues.empty()) {
            auto cr = crt(residues, moduli);
            r = cr.x; M = cr.M;
        }
        // Scan for the smallest prime in this class >= 3
        u64 k = 0;
        if (r < 3) k = (3 - r + M - 1) / M;
        else k = 0;
        while (true) {
            u64 cand = r + k * M;
            if (cand >= best) break;  // no better than current best
            if (cand < 3 || cand > 10000000000000000000ULL) { ++k; continue; }
            if (is_prime(cand) && check_a_n(cand, qs)) {
                best = cand;
                break;
            }
            ++k;
        }
    }
    return best;
}

int main() {
    // Cross-check: a(1..8) validate the method against known published values
    std::cout << "a(1) = " << find_a_n(1) << std::endl;
    std::cout << "a(2) = " << find_a_n(2) << std::endl;
    std::cout << "a(3) = " << find_a_n(3) << std::endl;
    std::cout << "a(4) = " << find_a_n(4) << std::endl;
    std::cout << "a(5) = " << find_a_n(5) << std::endl;
    std::cout << "a(6) = " << find_a_n(6) << std::endl;
    std::cout << "a(7) = " << find_a_n(7) << std::endl;
    std::cout << "a(8) = " << find_a_n(8) << std::endl;
    // Claim minimum: a(9)
    std::cout << "a(9) = " << find_a_n(9) << std::endl;
    return 0;
}
