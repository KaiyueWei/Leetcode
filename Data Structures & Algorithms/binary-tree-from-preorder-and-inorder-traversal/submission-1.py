# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ## preorder: root, left, right
        ## inorder: left, root, right
        n = len(preorder)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(preorder[0], None, None)
        val = preorder[0]
        root = TreeNode(val)
        ## find the index of root in inorder
        m = inorder.index(val)
        ## the left subtree: inorder[0:m], preorder[1:m+1]
        ## the right subtree: inorder[m+1:n], preorder[m+1:n]
        left = self.buildTree(preorder[1:m+1], inorder[0:m])
        right = self.buildTree(preorder[m+1:n], inorder[m+1:n])

        root.left = left
        root.right = right

        return root
        
        