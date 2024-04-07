from typing import List
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0

        for i in range(len(nums)):
            median = len(nums) // 2

            if (i >median): 
                res += max(0, k - nums[i]); 
            elif (i < median): 
                res += max(0, nums[i] - k)
            else: # i == median
                res += abs(k - nums[i]) 
        return res
    
print(Solution().minOperationsToMakeMedianK([2,5,6,8,5], 4))


        