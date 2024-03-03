class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squared_list = []
        for i in nums:
            squared_list.append(i * i)

        squared_list.sort()
        return squared_list
        
# other solutions

class Solution:
    def sortedSquares(self, nums):
        squares = [num * num for num in nums]
        squares.sort()
        return squares