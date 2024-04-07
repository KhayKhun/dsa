from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        longest,ic,dc = 1,1,1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]: 
                ic += 1
                dc = 1
            elif nums[i] < nums[i-1]: 
                dc += 1
                ic = 1  
            else: 
                ic = 1
                dc = 1
            
            longest = max(longest, ic, dc)
        
        return longest

print(Solution().longestMonotonicSubarray([1,4,3,3,2]))
