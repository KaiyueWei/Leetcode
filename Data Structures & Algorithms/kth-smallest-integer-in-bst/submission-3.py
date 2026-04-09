# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node, count):
            if node is None:
                return count, None
 
            count, res = inorder(node.left, count)
            if res is not None:
                return count, res
            count += 1
            if count == k:
                return count, node.val
            
            return inorder(node.right, count)
        
        _, res = inorder(root, 0)
        return res
        