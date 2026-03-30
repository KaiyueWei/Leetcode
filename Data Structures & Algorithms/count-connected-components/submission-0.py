class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ## transfer edges list to adjacency list
        graph = [ [] for _ in range(n)]
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        #count the connected components
        count = 0
        visited = set()
        def visit(node):
            visited.add(node)
            for nex in graph[node]:
                if nex not in visited:
                    visit(nex)
        
        for i in range(n):
            if i not in visited:
                visit(i)
                count += 1
        return count


        