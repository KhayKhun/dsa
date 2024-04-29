from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        prev = nums[0]
        index = 0
        pointer = 1
        
        while pointer < len(nums):
            index += 1
            while nums[pointer] == prev:
                if pointer == len(nums) - 1: return index
                pointer += 1
            
            prev = nums[pointer]
            nums[index],nums[pointer] = nums[pointer],nums[index]
            
            pointer += 1
        
        return index + 1