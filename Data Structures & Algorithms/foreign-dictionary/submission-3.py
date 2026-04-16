class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        for word in words:
            for c in word:
                graph[c] = []


        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            len_w1 = len(w1)
            len_w2 = len(w2)
            minLength = min(len_w1, len_w2)
            if len_w1 > len_w2 and w1[:minLength] == w2[:minLength]:
                return ""
            else:
                for j in range(minLength):
                    if w1[j] != w2[j]:
                        graph[w1[j]].append(w2[j])
                        break
        
        visited = set()
        visiting = set()

        def dfs(node):
            if node in visiting:
                return True
            if node in visited:
                return False
            
            visiting.add(node)

            for after_c in graph[node]:
                if dfs(after_c):
                    return True
            
            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return False

        
        res = []

        for c in graph.keys():
            if dfs(c):
                return ""
        res.reverse()

        return "".join(res)
                        

        
        