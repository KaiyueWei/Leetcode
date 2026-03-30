# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = deque()
        queue2 = deque()
        queue1.append(p)
        queue2.append(q)
        while queue1 and queue2:
            print(f'queue1, {len(queue1)}')
            print(f'queue2, {len(queue2)}')
            level_size1 = len(queue1)
            level_size2 = len(queue2)
            if level_size1 != level_size2:
                return False
            for _ in range(level_size1):
                node1 = queue1.popleft()
                node2 = queue2.popleft()
                if node1 == None and node2 == None:
                    continue
                if node1 != None and node2 == None:
                    return False
                if node1 == None and node2 != None:
                    return False
                if node1.val != node2.val:
                    return False
                ## Without enqueuing None, BFS would miss structural mismatches.
                queue1.append(node1.left)
                queue2.append(node2.left)
                queue1.append(node1.right)
                queue2.append(node2.right)
        return True
        