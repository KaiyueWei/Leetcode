# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def search(self, root: TreeNode, small: int, big: int) -> TreeNode:
        if root == None:
            return None
        
        if small <= root.val and big >= root.val:
            return root
        elif small > root.val:
            return self.search(root.right, small, big)
        elif big < root.val:
            return self.search(root.left, small, big)
               
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < q.val:
            small = p.val
            big = q.val 
        else:
            small = q.val
            big = p.val
        return self.search(root, small, big)
        
        

        