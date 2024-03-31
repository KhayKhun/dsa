class Solution:
    def count_alternating_subarrays(self,nums):
        n = len(nums)
        count = 0
        length = 1 

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                length += 1
            else:
                count += (length * (length + 1)) // 2
                length = 1

        count += (length * (length + 1)) // 2 

        return count

nums1 = [0, 1, 1, 1]
nums2 = [1, 0, 1, 0]

print(Solution().count_alternating_subarrays(nums1))  
print(Solution().count_alternating_subarrays(nums2)) 
