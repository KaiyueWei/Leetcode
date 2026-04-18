# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        longest = [float('-inf')]

        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left = max(left, 0)
            right = max(right, 0)
            cur = node.val + left + right
            longest[0] = max(longest[0], cur)
            return node.val + max(left, right)
        dfs(root)
        return longest[0]