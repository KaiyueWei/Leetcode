class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(pos):
            r, c = pos
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r,c))
            return 1 + dfs((r+1, c)) + dfs((r-1, c)) + dfs((r, c+1)) + dfs((r, c-1))

        area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = max(area, dfs((i,j)))
        return area

        