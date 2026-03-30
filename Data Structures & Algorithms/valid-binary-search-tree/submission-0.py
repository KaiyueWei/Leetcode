# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: Optional[TreeNode], minValue: int, maxValue) -> bool:
        if root == None:
            return True
        if root.val <= minValue:
            return False
        if root.val >= maxValue:
            return False
        
        return self.helper(root.left, minValue, root.val) and \
                self.helper(root.right, root.val, maxValue) 

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -math.inf, math.inf)
        
        