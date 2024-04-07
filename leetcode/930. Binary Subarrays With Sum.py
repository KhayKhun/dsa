from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res, current = 0, 0
        d = {0: 1}

        for i in nums:
            current += i
            dif = current - goal
            res += d.get(dif,0)

            d[current] = d.get(current,0) + 1
        return res