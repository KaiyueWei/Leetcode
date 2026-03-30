# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDia = [0]

        def dfs(root):
            if root == None:
                return 0
            leftSubtree = dfs(root.left)
            rightSubtree = dfs(root.right)
            curDia = leftSubtree + rightSubtree
            maxDia[0] = max(maxDia[0], curDia)
            return 1 + max(leftSubtree, rightSubtree)

        dfs(root)
        return maxDia[0]

        