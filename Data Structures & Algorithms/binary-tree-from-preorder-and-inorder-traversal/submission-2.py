# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(
        self,
        preorder: List[int],
        l: int,
        r: int,
        index_map: dict
    ) -> Optional[TreeNode]:

        # inorder range is empty
        if l > r:
            return None

        # root is always the first element in preorder
        val = preorder[0]
        root = TreeNode(val)

        # root index in inorder
        m = index_map[val]

        # number of nodes in left subtree
        left_size = m - l

        # build left subtree
        root.left = self.helper(
            preorder[1 : 1 + left_size],
            l,
            m - 1,
            index_map
        )

        # build right subtree
        root.right = self.helper(
            preorder[1 + left_size :],
            m + 1,
            r,
            index_map
        )

        return root

    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[TreeNode]:

        if not preorder:
            return None

        index_map = {val: i for i, val in enumerate(inorder)}

        return self.helper(
            preorder,
            0,
            len(inorder) - 1,
            index_map
        )
        
        