# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return 'X,'
        return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right)
    
    def helper(self, queue):
        if not queue:
            return 
        
        val = queue.popleft()
        if val == 'X':
            return None
        
        node = TreeNode(int(val))
        node.left = self.helper(queue)
        node.right = self.helper(queue)
        return node
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        queue = deque(data.split(','))
        return self.helper(queue)
    
