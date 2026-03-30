# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, minVal, maxVal) -> bool:
        if root == None:
            return True
        
        if root.val <= minVal:
            return False
        if root.val >= maxVal:
            return False
        return self.dfs(root.left, minVal, root.val) and \
                self.dfs(root.right, root.val, maxVal)
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -math.inf, math.inf)
        