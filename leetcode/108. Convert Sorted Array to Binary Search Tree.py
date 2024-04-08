# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return
        mid = len(nums)//2
        l = nums[:mid]
        r = nums[mid+1:]

        return TreeNode(nums[mid], self.sortedArrayToBST(l), self.sortedArrayToBST(r))

        