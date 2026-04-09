# Definition for a binary tree node.
from io import DEFAULT_BUFFER_SIZE
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = [float('-inf')]

        def helper(node):
            if node is None:
                return 0
            
            left_max = helper(node.left)
            right_max = helper(node.right)
            left_max = max(0, left_max)
            right_max = max(0, right_max)
            cur = node.val + left_max + right_max
            res[0] = max(res[0], cur)
            return node.val + max(left_max, right_max)
        helper(root)

        return res[0]
        