from typing import List
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primes = []
        def is_prime(n):
            if n <= 1:
                return False
            elif n <= 3:
                return True
            elif n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        for i in range(len(nums)):
            if is_prime(nums[i]): primes.append(i)
        return abs(max(primes) - min(primes))