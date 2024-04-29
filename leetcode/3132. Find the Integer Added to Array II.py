from typing import List
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        ans = float('-inf')
        nums1.sort()
        nums2.sort()

        def check(diff):
            i = 0
            for n2 in nums2:
                n1 = n2 + diff
                while i < m and nums1[i] != n1:
                    i += 1
                if i >= m:
                    return False
                i += 1
            return True

        for diff in [nums1[0] - nums2[0], nums1[1] - nums2[0], nums1[2] - nums2[0]]:
            if check(diff):
                ans = max(ans, diff)
        return -ans