# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        ## breadth-first search level by level 
        queue = []
        queue.append(root)
        while queue:
            cur = queue.pop(0)
            tmp1 = cur.right 
            tmp2 = cur.left
            cur.left = tmp1
            cur.right = tmp2
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return root





        