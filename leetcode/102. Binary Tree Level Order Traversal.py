class Solution:
    def levelOrder(self, root):
        if not root: return
        result = []
        # main recursive func
        def dive(node,index): 
            if not node: return
            if len(result) <= index: # Create a new list if the result[index] doesn't exists. This case will be occured everytime we dive down a level
                result.append([node.val])
            else: # If there is already a list at result[index], just append the value.
                result[index].append(node.val)
            # pass index + 1 if the node has children
            if node.left: dive(node.left, index + 1)
            if node.right: dive(node.right, index + 1)

        dive(root,0) # starting point. node:root, index:0

        return result
        