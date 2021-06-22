#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n == 1:
        print(0)
    elif n == 2:
        print(2)
    else:
        evenSum = 2
        first = 1
        second = 2
        third = 3
        while(first+second <= n):
            third = first + second
            if third%2 == 0:
                evenSum += third
            #print(third)
            first = second
            second = third
        print(evenSum)
