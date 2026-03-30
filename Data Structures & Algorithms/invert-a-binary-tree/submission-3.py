# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            cur = queue.popleft()
            tmp1, tmp2 = cur.left, cur.right
            cur.left = tmp2
            cur.right = tmp1
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return root





        


        