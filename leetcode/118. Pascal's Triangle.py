from math import factorial
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def getVals(x):
            n = x - 1
            return [int(factorial(n)/(factorial(i) * factorial(n - i))) for i in range(x)]

        return [getVals(i) for i in range(1, numRows + 1)]