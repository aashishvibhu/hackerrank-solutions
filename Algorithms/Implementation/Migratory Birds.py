#Migratory Birds Python code

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr_counter = Counter(arr)
    maximum_count = max(arr_counter.values())
    smallest = []
    for element, count in arr_counter.items():
        if count == maximum_count:
            smallest.append(element)
    return min(smallest)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
