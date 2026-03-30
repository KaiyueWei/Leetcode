# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self, root, k, count):
        if root is None:
            return None, count

        # left
        val, count = self.inOrder(root.left, k, count)
        if val is not None:
            return val, count

        # visit
        count += 1
        if count == k:
            return root.val, count

        # right
        return self.inOrder(root.right, k, count)

    def kthSmallest(self, root, k):
        val, _ = self.inOrder(root, k, 0)
        return val
        