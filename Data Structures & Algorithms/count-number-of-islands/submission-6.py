class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(pos):
            seen.add(pos)
            r, c = pos 

            for dr, dc in directions:
                newr = dr + r
                newc = dc + c 
                if 0 <= newr < n and 0 <= newc < m and \
                    (newr, newc) not in seen and grid[newr][newc] == "1":
                    dfs((newr, newc))
        
        for i in range(n):
            for j in range(m):
                if (i, j) not in seen and grid[i][j] == "1":
                    dfs((i, j))
                    count += 1
        return count

