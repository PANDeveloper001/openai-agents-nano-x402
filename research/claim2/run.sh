#!/usr/bin/env bash
# Build and run the blind re-derivation of pursekeeper/claims claim 2.
#
#   ./run.sh          -> b(1..12), the pass criterion's minimum (~25 s)
#   ./run.sh 13       -> also b(13), the claim's own next term (~3 min)
#
# Both fit the sandbox (10 min wall, 2 CPUs, 4 GB, no network).
set -euo pipefail
cd "$(dirname "$0")"
g++ -std=c++17 -O2 -o rederive rederive.cpp
./rederive "${1:-12}"
