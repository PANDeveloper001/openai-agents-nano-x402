#!/usr/bin/env bash
# Blind re-derivation of pursekeeper claim 8, written from the statement alone.
# Builds and runs everything; prints the six sequences the claim asks for, n = 7..12.
set -euo pipefail
cd "$(dirname "$0")"
g++ -O2 -std=c++17 -o rederive rederive.cpp
./rederive 12