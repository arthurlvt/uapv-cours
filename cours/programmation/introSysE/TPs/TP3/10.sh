#!/bin/bash
# return all even numbers from 0 to a value given as an argument
for i in $(seq 0 2 $1); do
    echo $i
done