# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node, count):
            if node is None:
                return None, count
            val, count = dfs(node.left, count)
            if val is not None:
                return val, count
            count += 1
            if count == k:
                return node.val, count
            return dfs(node.right, count)
        
        res, _ = dfs(root, 0)
        return res
        