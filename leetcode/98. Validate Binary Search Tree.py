from typing import Optional
class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return repr(self.val)
    
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def explore(node, f, t): # from < node < to
            if not node: return True 
            elif not (f < node.val and node.val < t): return False

            return explore(node.left,f,node.val) and explore(node.right,node.val,t)
        return explore(root,float('-inf'),float('inf'))