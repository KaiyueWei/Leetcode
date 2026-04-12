# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, prev):
            if node is None:
                return True, prev
            
            isValid, prev = dfs(node.left, prev)
            if not isValid:
                return False, prev
            if node.val <= prev:
                return False, prev
            prev = node.val

            return dfs(node.right, prev)
        
        isValid, _ = dfs(root, float('-inf'))
        return isValid
            
        