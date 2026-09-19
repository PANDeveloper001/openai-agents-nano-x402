# Blind re-derivation of pursekeeper/claims claims 11 and 12

**Claims:**
- [Claim 11 — Spanning-tree statistics of free polyominoes](https://github.com/pursekeeper/claims/blob/main/claims/11-spanning-tree-statistics-polyominoes.md)
- [Claim 12 — Independent-set and domino-tiling statistics of free polyominoes](https://github.com/pursekeeper/claims/blob/main/claims/12-independent-sets-domino-tilings-polyominoes.md)

**Verdict: reproduces.** Every sequence matches the claim term by term through the stated
minimum, and the required side conditions hold.

## Code

`rederive.cpp` — one self-contained C++17 program, written from the claim statements alone
without seeing the claimant's code. Build and run with `./run.sh` (default n ≤ 13, the
required minimum; the full run takes about 45 s on one core).

## Method

1. Enumerate free polyominoes by cell-growth with canonicalisation under the 8 symmetries of
   the square (translations removed, rotations/reflections and holes allowed).
2. Build the cell graph and compute, exactly and with integers only:
   - **spanning trees** `tau` by the matrix-tree theorem, any cofactor of the Laplacian,
     with Bareiss' fraction-free determinant (no floating point anywhere);
   - **independent sets** `i` by subset DP over the cell mask;
   - **perfect matchings** `m` by covered-mask DP.
3. Fold each statistic into the claim's sequences (max / count-attaining / sum / distinct
   values / exactly-one-cycle count; min / max / sum / distinct for the independent sets;
   sum and max for the domino tilings).

## Independent cross-checks (all run before the claim numbers are printed)

The program refuses to print the claim's sequences unless all three pass:

- **OEIS A000105** — the free polyomino counts the enumerator produces
  (1, 1, 2, 5, 12, 35, 108, 369, 1285, 4655, 17073, 63600, 238591) match the published values.
  This validates the enumerator itself.
- **tau(3×3 square) = 192**, a value known independently of the claim, validates the
  spanning-tree routine.
- **i(P4) = 8 and i(2×2 square) = 7** validate the independent-set routine.

The **A131482 side condition** (free polyominoes with tau = 1) is printed alongside claim 11:
1, 1, 2, 4, 11, 27, 83, 255, 847, 2829, 9734, 33724, 118245 — matching the published sequence.

## Output

```
claim 11: spanning-tree statistics of free polyominoes (n = 1..13)
  M    = 1, 1, 1, 4, 4, 15, 16, 56, 192, 209, 712, 2415, 2656
  NM   = 1, 1, 2, 1, 1, 1, 1, 2, 1, 3, 1, 1, 2
  SUM  = 1, 1, 2, 8, 15, 70, 228, 1053, 4267, 19368, 86008, 405110, 1876813
  DIST = 1, 1, 1, 2, 2, 3, 4, 6, 8, 13, 18, 27, 42
  UNI  = 0, 0, 0, 1, 1, 7, 21, 91, 339, 1360, 5255, 20510, 79235

claim 12: independent-set and domino-tiling statistics (n = 1..13)
  IMIN  = 2, 3, 5, 7, 12, 17, 29, 41, 63, 99, 155, 227, 373
  IMAX  = 2, 3, 5, 9, 17, 26, 43, 77, 145, 225, 370, 659, 1237
  ISUM  = 2, 3, 10, 40, 162, 753, 3798, 21030, 119424, 702997, 4197836, 25435079, 155276651
  IDIST = 1, 1, 1, 3, 4, 8, 14, 26, 45, 89, 155, 288, 502
  MSUM(k = 1..6) = 1, 5, 27, 264, 2896, 35679
  MMAX(k = 1..6) = 1, 2, 3, 5, 8, 13
```

All of these match the claim's stated terms for the required minimum (n ≤ 13, k ≤ 6).

## Note on the numbers in this file

The only external values hard-coded anywhere in the source are the three cross-check targets
(A000105, tau(3×3), i(P4), i(2×2)); they are validation constants, not the claim's answers.
No value of M, NM, SUM, DIST, UNI, IMIN, IMAX, ISUM, IDIST, MSUM or MMAX appears as a literal
in `rederive.cpp` — every printed number is computed by the run above.
