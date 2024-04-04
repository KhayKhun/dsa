from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack, stack2 = [root1], [root2]
        leaves, leaves2 = [], []

        while len(stack) > 0:
            node = stack.pop()
            if not(node.left or node.right): leaves.append(node.val)

            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        while len(stack2) > 0:
            node = stack2.pop()
            if not(node.left or node.right): leaves2.append(node.val)

            if node.left: stack2.append(node.left)
            if node.right: stack2.append(node.right)
        
        return leaves == leaves2