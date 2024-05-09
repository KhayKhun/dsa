class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        s = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in s:
                total = 1
                current = n

                while current + 1 in s:
                    total += 1
                    current += 1
                longest = max(longest,total)

        return longest

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in s:
                total = 1

                while n + total in s:
                    total += 1
                longest = max(longest,total)

        return longest
