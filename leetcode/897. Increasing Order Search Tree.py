class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return '(%s)' %self.val

def DepthFirstValues(node):
            if not node: return []
            print(node.val)
            return DepthFirstValues(node.right) + [node.val] + DepthFirstValues(node.left)
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
  
d.left = b
b.left = a
b.right = c
d.right = e
e.right = f

class Solution:
    def increasingBST(self, root):
        if not root:return
        values = self.getVal(root)
        
        resultNode = TreeNode(values.pop())
        current = resultNode
        while len(values) > 0:
            current.right = TreeNode(values.pop())
            current = current.right

        return resultNode
    
    def getVal(self,node):
        if not node: return []
        return self.getVal(node.right) + [node.val] + self.getVal(node.left)

result = Solution().increasingBST(d)
print(result)
print(DepthFirstValues(result))