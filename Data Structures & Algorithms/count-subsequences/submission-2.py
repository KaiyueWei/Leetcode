class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        count = [0]

        n = len(s)
        m = len(t)

        def backtrack(i, j):
            if j == m:
                count[0] += 1
                return 
            if i == n:
                return 
            
            # consider the current
            if s[i] == t[j]:
                backtrack(i+1, j+1)
            # not take the current 
            backtrack(i+1, j)
        backtrack(0, 0)
        return count[0]
        