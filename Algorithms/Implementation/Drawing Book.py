#Drawing Book - Python Code

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    even = True if n%2 == 0 else False
    if p in (n,1) or (not even and p == n-1):
        return 0
    last_odd = n-1 if even else n
    p_even = True if p%2 == 0 else False
    p_left = p if p_even else p-1
    p_right = p+1 if p_even else p
    return min((p_left + 1)// 2, (n - p_right + 1) // 2)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
