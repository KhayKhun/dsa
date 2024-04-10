from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self._isSymmetric(root.left,root.right)

    def _isSymmetric(self,r1,r2):
        if not r1 and not r2: return True # both None
        if not r1 or not r2: return False # 1 of them is None
        if r1.val != r2.val: return False

        return self._isSymmetric(r1.left,r2.right) and self._isSymmetric(r1.right,r2.left)




        