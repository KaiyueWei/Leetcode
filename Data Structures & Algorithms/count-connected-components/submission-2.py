class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #transfer a edge list to an adjacency list
        graph = [[] for _ in range(n)]
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        count = 0
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count
        