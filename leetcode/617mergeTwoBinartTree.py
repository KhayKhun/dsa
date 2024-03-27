class TreeNode:
    def __init__(self,val) -> None:        
        self.val = val
        self.left = None
        self.right = None
    def __repr__(self) -> str:
        return '%s' %self.val

def depth_first_values_recursive(x):
    if not x:
        return []
    return [x.val] + depth_first_values_recursive(x.left) + depth_first_values_recursive(x.right)

a = TreeNode(1)
b = TreeNode(3)
c = TreeNode(2)
d = TreeNode(5)
  
a.left = b
b.left = c
c.left = d

w = TreeNode(2)
x = TreeNode(1)
y = TreeNode(3)
z = TreeNode(4)
z1 = TreeNode(7)
  
w.left = x
x.left = y
y.right = z
z.right = z1
class Solution:
    def mergeTrees(self, root1,root2):
        if not root1 and root2:
            root1 = root2
            return root1
        
        if root1 and root2:
            root1.val += root2.val

            root1.left = self.mergeTrees(root1.left,root2.left)
            root1.right = self.mergeTrees(root1.right,root2.right)

        return root1
        

c = TreeNode(1)
d= TreeNode(1)
d.left = TreeNode(2)

print('root1:',depth_first_values_recursive(a))
print('root2:',depth_first_values_recursive(w))
result = Solution().mergeTrees(a,w)
print('result:',depth_first_values_recursive(result))