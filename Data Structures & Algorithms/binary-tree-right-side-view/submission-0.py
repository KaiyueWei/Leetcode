# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            cur = None
            for i in range(level_size):
                print(level_size)
                print(f"i: {i}")
                node = queue.popleft()
                print(f"val: {node.val}")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == level_size - 1:
                    cur = node
            res.append(cur.val)
        return res