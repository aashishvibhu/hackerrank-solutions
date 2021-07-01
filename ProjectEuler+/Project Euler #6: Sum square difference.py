#!/bin/python3

#Project Euler #6: Sum square difference - Python code

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    square_of_sum = int(pow((n*(n+1))/2, 2))
    sum_of_square = int(n*(n+1)*(2*n+1)/6)
    print(square_of_sum - sum_of_square)
