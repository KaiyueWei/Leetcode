# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root:Optional[TreeNode], res: List[List[int]], depth: int) -> List[List[int]]:
        if root == None:
            return None
        if len(res) == depth:
            res.append([])
        
        res[depth].append(root.val)
        self.dfs(root.left, res, depth + 1)
        self.dfs(root.right, res, depth + 1)

        return res

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        depth = 0
        self.dfs(root, res, depth)
        return res




        