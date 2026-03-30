# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self, root: Optional[TreeNode], prev: int) -> (bool, int):
        if root == None:
            return True, prev
        
        valid, prev = self.inOrder(root.left, prev)
        if not valid:
            return False, prev
        
        if root.val <= prev:
            return False, prev
        
        prev = root.val

        return self.inOrder(root.right, prev)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid, _ = self.inOrder(root, -math.inf)
        return valid
        
        
        