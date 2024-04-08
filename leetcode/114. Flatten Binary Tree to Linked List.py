class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return '(%s)' %self.val
# Input: nums = [3,2,1,6,0,5]
# Output: [6,3,5,null,2,0,null,null,1]

def depth_first_values_recursive(x):
    if not x:
        return [None]
    return [x.val] + depth_first_values_recursive(x.left) + depth_first_values_recursive(x.right)
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
  
a.left = b
b.left = c
b.right = d
a.right = e
e.right = f

class Solution:
    def flatten(self, root):
        def main(node):
            if not node: return
            if node.left:
                right = node.right
                
                node.right = main(node.left)
                current = node.left
                while current.right:
                    current = current.right
                current.right = right
                node.left = None
            if node.right: main(node.right)
            
            return node
        
        main(root)
            
print('start:',depth_first_values_recursive(a))
result = Solution().flatten(a)
print('end:',depth_first_values_recursive(a))


        