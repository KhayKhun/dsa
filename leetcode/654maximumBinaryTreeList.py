# Definition for a binary tree node.
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

class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums: return
        left,value,right = self.split(nums,nums.index(max(nums)))

        return self.main(left,value,right)

    def main(self,left,value,right):
        current = TreeNode(value)
        current.left = self.constructMaximumBinaryTree(left)
        current.right = self.constructMaximumBinaryTree(right)
        return current

    def split(self,nums,target):
        return nums[:target], nums[target], nums[target + 1:]
        
    
n = [3,2,1,6,0,5]

s= Solution()
result = s.constructMaximumBinaryTree(n)
print(result)
print(depth_first_values_recursive(result))
