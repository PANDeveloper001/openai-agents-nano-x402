# Blind re-derivation of pursekeeper/claims claim 2

**Claim:** Derangements avoiding the pattern 4321 (the sequence b(n) in
[`pursekeeper/claims/claims/02-derangements-avoiding-4321.md`](https://github.com/pursekeeper/claims/blob/main/claims/02-derangements-avoiding-4321.md)).

**Verdict: reproduces.** b(1..12) matches the stated minimum term by term, and the run also
confirms the claim's next term b(13) = 40267062.

## Code

`rederive.cpp` — one self-contained C++17 program, written from the claim statement alone
without seeing the claimant's code. Build and run with `./run.sh` (compile + execute).

```
$ ./run.sh
...
cross-check PASSED

b( 1) = 0
b( 2) = 1
...
b(12) = 6201974
b(13) = 40267062

b(1..13) = 0, 1, 2, 8, 34, 163, 842, 4616, 26530, 158496, 977974, 6201974, 40267062
```

## Method

b(n) counts permutations p of {1..n} that are fixed-point-free (p(i) != i) and contain no
i < j < k < l with p(i) > p(j) > p(k) > p(l) (no decreasing subsequence of length 4, i.e. p
avoids the classical pattern 4321).

The program builds permutations position by position and keeps, at each filled position, the
length `L` of the longest decreasing subsequence ending there. Because extending a prefix can
only ever *lengthen* a decreasing subsequence, a prefix whose `L` reaches 4 already contains a
4321 pattern and every extension of it does too — so the branch is discarded immediately. The
fixed-point condition is applied on the same descent. The search space that survives this
pruning is small: the full run to n=13 finishes in about 4 minutes on one core and to the
required minimum (n=12) in about 23 seconds, well inside the sandbox's 10-minute wall clock.

**No answer literals for the claim.** Every value of b(n) printed above is computed by the
enumerator; the b(n) sequence appears nowhere in the source as a constant.

## Independent cross-check

The same enumerator is run a second time with the derangement condition switched off, where
it must reproduce **OEIS A005802** (4321-avoiding permutations), a sequence known independently
of this claim:

```
n:  1     2     3     4      5      6       7        8         9         10
    1,    2,    6,    23,   103,   513,   2761,   15767,    94359,    586590,
n:  11         12          13
    3763290,   24792705,   167078577
```

All thirteen terms match the OEIS values exactly (`cross-check PASSED`). This is what makes the
result meaningful: it shows the enumerator counts the right family, so the b(n) terms are not
an artefact of a mis-built search. The A005802 values in the source are the cross-check target,
not the claim's answer — the claim's sequence is never hard-coded.

## Reproducing the published terms

The claim is published in full at
[`pursekeeper/claims/claims/02-derangements-avoiding-4321.md`](https://github.com/pursekeeper/claims/blob/main/claims/02-derangements-avoiding-4321.md),
including the terms beyond this run and the pass criterion (minimum b(1..12)). They are
deliberately not repeated here: this directory is the re-derivation, and the only numbers it
prints are the ones the program computed.
