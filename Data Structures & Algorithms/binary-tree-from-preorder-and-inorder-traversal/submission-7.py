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

        pre = [0]

        def dfs(l, r):
            if l > r:
                return None
            val = preorder[pre[0]]
            node = TreeNode(val)
            index = inorder_map[val]

            pre[0] += 1

            node.left = dfs(l, index-1)
            node.right = dfs(index+1, r)
            return node
        
        return dfs(0, len(inorder)-1)
        