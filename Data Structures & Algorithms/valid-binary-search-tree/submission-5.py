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
            is_valid, prev = dfs(node.left, prev)
            if not is_valid:
                return False, prev
            if node.val <= prev:
                return False, node.val
            prev = node.val
            return dfs(node.right, prev)
        
        is_valid, _ = dfs(root, float('-inf'))
        return is_valid

        