class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        count = [0]

        n = len(s)
        m = len(t)
        dp = {}
        def backtrack(i, j):
            if j == m:
                return 1
            if i == n:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            # consider the current
            res = backtrack(i+1, j)
            if s[i] == t[j]:
                res += backtrack(i+1, j+1)
            # not take the current 
            dp[(i, j)] = res
            return dp[(i, j)]
        return backtrack(0,0)
        
        