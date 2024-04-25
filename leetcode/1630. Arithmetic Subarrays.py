from typing import List
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], lefts: List[int], rights: List[int]) -> List[bool]:
        res = [False] * len(lefts)

        def isValid(l, r):
            diff = None
            sliced = nums[l:r+1]
            sliced.sort()
            for i in range(len(sliced) - 1):
                if diff == None:
                    diff = sliced[i] - sliced[i+1]
                    continue
                
                if sliced[i] - sliced[i+1] != diff: return False

            return True
        
        for i in range(len(lefts)):
            if isValid(lefts[i],rights[i]): res[i] = True

        return res

        