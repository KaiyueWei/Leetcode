class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Make Graph
        charGraph = {}
        # 'b': ['a', 'c']
        for word in words:
            for c in word:
                charGraph[c] = []
        # Populate Graph
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            minLength = min(len(w1), len(w2))
            if len(w1) >len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            for j in range(minLength):
                if w1[j] != w2[j]:
                    # ape, apr
                    charGraph[w1[j]].append(w2[j])
                    break

        visited = set()
        visiting = set()
        res = []
        # DFS
        def isCycle(c):
            if c in visiting:
                return True
            if c in visited:
                return False
            # mark as visiting
            visiting.add(c)
            for nei in charGraph[c]:
                if isCycle(nei):
                    return True
            visited.add(c)
            visiting.remove(c)
            res.append(c)
            return False
        # Iterate Graph
        for c in charGraph:
            if isCycle(c):
                return ""
        res.reverse()
        return "".join(res)