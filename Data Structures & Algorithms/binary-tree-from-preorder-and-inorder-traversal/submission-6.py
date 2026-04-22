# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder is None or inorder is None:
            return None
        
        inorder_map = {value:index for index, value in enumerate(inorder)}
        pre_index = [0]
        
        def dfs(l, r):
            if l > r:
                return None
            
            node = TreeNode(preorder[pre_index[0]])
            root_index = inorder_map[preorder[pre_index[0]]]
            pre_index[0] += 1
            left_size = root_index - l
            
            node.left = dfs(l, root_index-1)
            node.right = dfs(root_index+1, r)
            return node
        
        return dfs(0, len(inorder)-1)
        