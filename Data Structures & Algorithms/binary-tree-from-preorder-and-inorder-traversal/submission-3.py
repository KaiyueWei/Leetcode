# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self, preorder, l, r, index_map) ->Optional[TreeNode]:
        if l > r:
            return None
        val = preorder[0]
        root = TreeNode(val)

        root_index = index_map[val]

        ## number of the nodes in the leftsubtree
        left_size = root_index - l

        root.left = self.helper(preorder[1:1+left_size], l, root_index - 1, index_map)
        root.right = self.helper(preorder[1+left_size:], root_index + 1, r, index_map)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder == None or inorder == None:
            return None
        index_map = {val: index for index, val in enumerate(inorder)}
        return self.helper(preorder, 0, len(inorder) - 1, index_map)
        