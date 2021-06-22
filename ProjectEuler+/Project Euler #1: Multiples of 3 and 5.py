#!/bin/python3

import sys
import math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())-1
   
    number_of_3 = (n) // 3
    sum_of_3 = 3*number_of_3*(number_of_3+1)//2
        
    
    number_of_5 = (n) // 5
    sum_of_5 = 5*number_of_5*(number_of_5+1)//2
        
    
    number_of_15 = (n) // 15
    sum_of_15 = 15*number_of_15*(number_of_15+1)//2
    
    print(int(sum_of_5 + sum_of_3 - sum_of_15))
