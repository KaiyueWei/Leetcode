# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf')]

        def dfs(node, res) -> int:
            if node == None:
                return 0
            left_max = dfs(node.left, res)
            right_max = dfs(node.right, res)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)
            # splitting at the node
            cur = node.val + left_max + right_max
            res[0] = max(cur, res[0])
            #no splitting
            return node.val + max(left_max, right_max)
        dfs(root, res)
        return res[0]