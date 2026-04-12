# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        index_map = {val: i for i, val in enumerate(inorder)}

        def dfs(l, r, preorder_index):
            if l > r:
                return None

            root_val = preorder[preorder_index]
            root = TreeNode(root_val)

            mid = index_map[root_val]
            left_size = mid - l

            root.left = dfs(l, mid - 1, preorder_index + 1)
            root.right = dfs(mid + 1, r, preorder_index + 1 + left_size)

            return root

        return dfs(0, len(inorder) - 1, 0)



        