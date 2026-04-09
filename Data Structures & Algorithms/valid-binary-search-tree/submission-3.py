# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inorder(node, prev):
            if node is None:
                return True, prev
            
            valid, prev = inorder(node.left, prev)
            if not valid:
                return False, prev
                
            if node.val <= prev:
                return False, node.val
            prev = node.val
            
            return inorder(node.right, prev)
        
        valid, prev = inorder(root, float('-inf'))
        return valid
        