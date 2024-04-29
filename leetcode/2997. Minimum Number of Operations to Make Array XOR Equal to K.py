from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = 0
        for num in nums: total ^= num

        n = total ^ k

        count = 0
        while n:
            count += n & 1
            n >>= 1

        return count
        