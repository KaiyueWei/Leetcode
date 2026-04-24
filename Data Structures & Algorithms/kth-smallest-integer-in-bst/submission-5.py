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
                return count, None
            count, val = dfs(node.left, count)
            if val is not None:
                return count, val
            count += 1
            if count == k:
                return count, node.val
            return dfs(node.right, count)

        _, val = dfs(root, 0)
        return val        