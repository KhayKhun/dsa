from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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

            _newLeft = TreeNode(val)
            _newLeft.left = node.left
            node.left = _newLeft

            _newRight = TreeNode(val)
            _newRight.right = node.right
            node.right = _newRight

        return root
                