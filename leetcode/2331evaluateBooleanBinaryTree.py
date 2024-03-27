class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return str(self.val)

# 0 = False
# 1 = True
# 2 = or
# 3 = and

a = TreeNode(2)  #           OR                                       
b = TreeNode(0)  #     true     AND     
c = TreeNode(3)  #                       
d = TreeNode(0)  #           true   false            
e = TreeNode(1)  #                         

a.left = b
a.right = c
c.left = d
c.right = e

class Solution:
    def evaluateTree(self, root):
        if root.val == 2: return self.evaluateTree(root.left) or self.evaluateTree(root.right) 
        elif root.val == 3: return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        return bool(root.val)
       

print('start:',a)
result = Solution().evaluateTree(TreeNode(0))
print('result:',result)