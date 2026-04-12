# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def dfs(root, cur_max):
            if root is None:
                return
            
            if cur_max <= root.val:
                res[0] += 1
                cur_max = root.val
            
            dfs(root.left, cur_max)
            dfs(root.right, cur_max)

        dfs(root, float('-inf'))
        return res[0]



        