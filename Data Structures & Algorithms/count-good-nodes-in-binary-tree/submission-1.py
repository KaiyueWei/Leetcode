# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def dfs(node, max):
            if node is None:
                return 
            if node.val < max:
                dfs(node.left, max)
                dfs(node.right, max)
                return
            else:
                res[0] += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)
                return 
        dfs(root, float('-inf'))
        return res[0]