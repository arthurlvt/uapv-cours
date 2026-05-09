#!/bin/bash
# return the multiplication table of a value given as an argument
for i in $(seq 1 10); do
    echo "$1 x $i = $(($1 * $i))"
done