from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        stack = [(chr(97+root.val),root)]
        res = ''
        while stack:
            path, node = stack.pop()
            print(path)
            if not (node.left or node.right):
                if res == '': res = path
                else: res = min(res,path)
                continue
            
            if node.left: stack.append((chr(97+node.left.val)+path,node.left))
            if node.right: stack.append((chr(97+node.right.val)+path,node.right))
        
        return res

        