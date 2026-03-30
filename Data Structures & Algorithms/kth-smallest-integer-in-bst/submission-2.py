# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, count, res, k)->None:
        if node == None:
            return 
        self.dfs(node.left, count, res, k)
        count[0] += 1
        if k == count[0]:
            res[0] = node.val
        self.dfs(node.right, count, res, k)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        res = [0]
        self.dfs(root, count, res, k)
        return res[0]
        