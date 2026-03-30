# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'X' + ','
        val = str(root.val)
        print(f'val:{val}')
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return val + ',' + left + right
        
    # Decodes your encoded data to tree.
    def helper(self, queue:deque) -> Optional[TreeNode]:
        val = queue.popleft()
        if val == 'X':
            return None
        root = TreeNode(int(val))
        root.left = self.helper(queue)
        root.right = self.helper(queue)
        return root
    def deserialize(self, data: str) -> Optional[TreeNode]:
        queue = deque(data.split(','))
        return self.helper(queue)


