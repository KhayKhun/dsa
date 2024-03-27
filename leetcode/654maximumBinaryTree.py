class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return '(%s)' %self.val

def depth_first_values_recursive(x):
    if not x:
        return [None]
    return [x.val] + depth_first_values_recursive(x.left) + depth_first_values_recursive(x.right)

x = TreeNode(3)
x.left = TreeNode(2)
x.left.left = TreeNode(1)
x.left.left.left = TreeNode(6)
x.left.left.left.left = TreeNode(0)
x.left.left.left.left.left = TreeNode(5)

class Solution:
    elem = None
    prev = None
    def constructMaximumBinaryTree(self, nums):
        if not nums: return
        previous,greatestNode,next = self.getGreatestNode(nums)
        self.elem, self.prev = None,None
        # print(previous,greatestNode.left,next)

        greatestNode.left = self.constructMaximumBinaryTree(previous)
        greatestNode.right = self.constructMaximumBinaryTree(next)


        return greatestNode
    
    def getGreatestNode(self,root):
        target = self.getMax(root)
        def find(item):
            if not item: return
            if item.val == target:
                self.elem = item
                return self.elem
            if item.left:
                self.prev = item
                find(item.left) 
            
        find(root)
        if self.prev: self.prev.left = None #diconnect with node
        else: root = None
        return root,self.elem,self.elem.left  


    def getMax(self,root):
        if not root: return 0
        return max(root.val, self.getMax(root.left),self.getMax(root.right))


s = Solution()
result = depth_first_values_recursive(x)
print(result)
ass = s.constructMaximumBinaryTree(x)
print(depth_first_values_recursive(ass))
print(type(3))