class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0]*m for _ in range(n)]

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            best = 1

            for dr, dc in directions:
                r, c = i + dr, j + dc
                if 0 <= r < n and 0 <= c < m and matrix[r][c] > matrix[i][j]:
                    best = max(best, 1 + dfs(r,c))

            dp[i][j] = best
            return best

        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i,j))

        return ans
        