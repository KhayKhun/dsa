from typing import List
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        mid = len(nums) // 2

        for i in range(len(nums)):
            if (i < mid): 
                res += max(0, nums[i] - k)
            elif (i > mid): 
                res += max(0, k - nums[i]); 
            else: # i == mid
                res += abs(k - nums[i]) 
        return res
    
print(Solution().minOperationsToMakeMedianK([2,5,5,6,8], 4))


        