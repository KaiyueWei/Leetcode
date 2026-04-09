# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        index_map = {v: i for i, v in enumerate(inorder)}
        pre_i = [0]

        def build(in_left, in_right):
            if in_left > in_right:
                return None

            root_val = preorder[pre_i[0]]
            pre_i[0] += 1

            root = TreeNode(root_val)
            mid = index_map[root_val]

            root.left = build(in_left, mid - 1)
            root.right = build(mid + 1, in_right)

            return root

        return build(0, len(inorder) - 1)
        
        