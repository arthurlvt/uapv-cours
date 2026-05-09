#!/bin/bash
# return the sum of numbers from 0 to a value given as an argument
for i in $(seq 0 $1); do
    sum=$((sum + i))
done
echo "Sum of numbers from 0 to $1 is: $sum"
