# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSametree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.isSametree(root.right, subRoot.right) and \
                    self.isSametree(root.left, subRoot.left)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        if subRoot == None:
            return True
        
        if self.isSametree(root, subRoot):
            return True
        
        return self.isSubtree(root.right, subRoot) or \
                self.isSubtree(root.left, subRoot)
        
        