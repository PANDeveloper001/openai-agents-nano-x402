#!/bin/bash
set -e
g++ -O2 -std=c++17 -Wall -Wextra -o rederive rederive.cpp
./rederive
