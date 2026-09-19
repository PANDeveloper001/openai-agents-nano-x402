#!/usr/bin/env bash
# Build and run the blind re-derivation of pursekeeper/claims claims 11 and 12.
#
#   ./run.sh          -> n = 1..13 (minimum), ~2-5 minutes
#   ./run.sh 14       -> also n = 14, takes longer
set -euo pipefail
cd "$(dirname "$0")"
g++ -std=c++17 -O2 -march=native -o rederive rederive.cpp
./rederive "${1:-13}"