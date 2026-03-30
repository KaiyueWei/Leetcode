class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        res = 0

        def dfs(i, j, prev):
            if i < 0 or j < 0 or i >= n or j >= m or matrix[i][j] <= prev:
                return 0

            cur = matrix[i][j]
            best = 0

            for dr, dc in directions:
                best = max(best, dfs(i+dr, j+dc, cur))

            return 1 + best

        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j, float('-inf')))

        return res



        