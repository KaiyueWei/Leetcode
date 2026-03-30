class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #make a graph using adjacency list
        #key is the character: value is a list of characters come after the key
        graph = {}
        for word in words:
            for c in word:
                graph[c] = []
        ##populate the graph
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            minLength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            for j in range(minLength):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break

        #DFS
        res = []
        visiting = set()
        visited = set()
        def dfs(node):
            if node in visiting:
                return True
            if node in visited:
                return False
            visiting.add(node)
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
            visited.add(node)
            visiting.remove(node)
            res.append(node)
            return False
        
        for c in graph:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
                    
        