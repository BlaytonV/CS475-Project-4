#!/bin/bash

OUTFILE="results.txt"
> $OUTFILE  # Clear output

SIZES=(1024 4096 16384 65536 262144 1048576 4194304 8388608)

for size in "${SIZES[@]}"
do
    echo "Testing ARRAYSIZE=$size"
    g++ -DARRAYSIZE=$size -fopenmp -o all04 all04.cpp
    ./all04 >> $OUTFILE 2>&1
done

echo "Done. Results saved to $OUTFILE"
