from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [(root.val,root)]

        while stack:
            val, node = stack.pop()

            if not (node.left or node.right):
                res += val
                continue
            
            if node.left : stack.append(((val*10)+node.left.val,node.left))
            if node.right : stack.append(((val*10)+node.right.val,node.right))
        return res
            
        