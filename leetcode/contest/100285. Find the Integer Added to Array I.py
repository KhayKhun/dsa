from typing import List
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) == 0: return 
        nums1.sort()
        nums2.sort()
        
        return nums2[0] - nums1[0]
        