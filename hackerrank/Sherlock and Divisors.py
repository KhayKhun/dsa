#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisors' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def divisors(n):
    if n%0: return 0
    
    count = 0
    sqrt_n = int(n ** 0.5)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            if i % 2 == 0:
                count += 1
            if i != n // i and (n // i) % 2 == 0:  # Check for the other divisor if it's different
                count += 1
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = divisors(n)

        fptr.write(str(result) + '\n')

    fptr.close()
