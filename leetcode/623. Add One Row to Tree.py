from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1: return TreeNode(val,root)
        stack = [(1,root)]
        while stack:
            d, node = stack.pop()

            if d + 1 != depth:
                if node.left: stack.append((d + 1,node.left))
                if node.right: stack.append((d + 1,node.right))
                continue

            node.left = TreeNode(val, left=node.left) if node.left else TreeNode(val)
            node.right = TreeNode(val, right=node.right) if node.right else TreeNode(val)

        return root
                