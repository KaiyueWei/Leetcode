class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        ## create a graph
        ## key: letter, value: list of letters that come after
        graph = {}
        for word in words:
            for c in word:
                graph[c] = []
        
        ## populate the graph
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            len_w1 = len(w1)
            len_w2 = len(w2)
            minLength = min(len_w1, len_w2)
            if len_w1 > len_w2 and w1[:minLength] == w2[:minLength]:
                return ""
            for j in range(minLength):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break
        visiting = set()
        visited = set()
        res = []
        ## dfs traverse
        def dfs(c:str) -> bool:
            if c in visiting:
                return True
            if c in visited:
                return False
            visiting.add(c)
            for after in graph[c]:
                if dfs(after):
                    return True
            visited.add(c)
            visiting.remove(c)
            res.append(c)
            return False

        ## entry points
        for c in graph:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
        