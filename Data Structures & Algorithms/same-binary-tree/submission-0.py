# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base case
        if q == None and p != None:
            return False
        if q != None and p == None:
            return False
        if q == None and p == None:
            return True
        if p.val != q.val:
            return False
        
        if not self.isSameTree(p.left, q.left):
            return False
        if not self.isSameTree(p.right, q.right):
            return False
        
        return True
        