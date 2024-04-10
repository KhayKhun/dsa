from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m -= 1 # index tracker for nums1
        n -= 1 # index tracker for nums2
        i = len(nums1) - 1

        while m >= 0 and n >= 0:
            # nums1 is greater
            if nums1[m] >= nums2[n]:
                nums1[i] = nums1[m] # put in the back
                m -= 1
            else:
                nums1[i] = nums2[n] # put in the back
                n -= 1
            i -= 1
        
        if n >= 0 and m < 0:
            for i in range(n + 1):
                nums1[i] = nums2[i]


        