from collections import defaultdict
import math
import os
import random
import re
import sys

# bruh

# def solve(balls):
#     return sum(balls) / 2

def solve(balls):
    d = defaultdict(int)

    def exploreSums(total,l):
        if len(l) == 0: 
            d[total] += 1
            return
        val = l[0]
        newList = l[1:]

        exploreSums(total + 0,newList)
        exploreSums(total + val,newList)
    exploreSums(0, balls)

    def ExpectedVal(count):
        total = 0

        for key, val in d.items():
            total += (key * val / count)
        return total
    
    return ExpectedVal(2**len(balls))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    balls_count = int(input().strip())

    balls = []

    for _ in range(balls_count):
        balls_item = int(input().strip())
        balls.append(balls_item)

    result = solve(balls)

    fptr.write(str(result) + '\n')

    fptr.close()
