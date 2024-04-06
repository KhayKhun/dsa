from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, current = 0,0
        d = {0: 1}
        for i in nums:
            current += i
            diff = current - k

            res += d.get(diff,0)
            d[current] = d.get(current,0) + 1
        return res
        