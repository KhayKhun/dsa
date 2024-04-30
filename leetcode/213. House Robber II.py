from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self, n: List[int]) -> int:
        rob1, rob2 = 0,0
        for n in n:
            best = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = best
        return rob2
        