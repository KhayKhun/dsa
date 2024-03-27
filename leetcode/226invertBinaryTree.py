class Node:
    def __init__(self,val) -> None:        
        self.val = val
        self.left = None
        self.right = None
    def __repr__(self) -> str:
        return '%s' %self.val

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(0)
  
a.right = b
a.right = c
b.left = d
b.right = e
c.right = f
class Solution:
    def invertTree(self, root):
        if root is None: return root
        stack = [root]
        while len(stack) > 0:
            current = stack.pop()
            left = current.left #2
            right = current.right #none
            if current.left or right:
                current.left = right #none
                if(current.left): stack.append(right)
            if current.right or left:
                current.right = left
                if(current.right): stack.append(left)

        return root
        
s = Solution()
print(a,a.left,a.right)
print(s.invertTree(a))
print(a,a.left,a.right)

#other's solution. wtf
class Solution(object):
    def invertTree(self, root):
        # Base case...
        if root == None:
            return root
        # swapping process...
        root.left, root.right = root.right, root.left
        # Call the function recursively for the left subtree...
        self.invertTree(root.left)
        # Call the function recursively for the right subtree...
        self.invertTree(root.right)
        return root     # Return the root...