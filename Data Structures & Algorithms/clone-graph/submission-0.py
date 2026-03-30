"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        queue = deque()
        oldToNew = {}
        oldToNew[node] = Node(node.val)
        queue.append(node)
        while queue:
            cur = queue.popleft()
            curCopy = oldToNew.get(cur, None)
            if curCopy == None:
                curCopy = Node(cur.val)
                oldToNew[cur] = curCopy
            for neighbor in cur.neighbors:
                neiCopy = oldToNew.get(neighbor, None)
                if neiCopy == None:
                    neiCopy = Node(neighbor.val)
                    oldToNew[neighbor] = neiCopy
                    queue.append(neighbor)
                curCopy.neighbors.append(neiCopy)
        
        return oldToNew[node]
        