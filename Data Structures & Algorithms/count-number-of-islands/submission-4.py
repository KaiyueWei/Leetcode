class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: 
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            visited.add((r, c))
            for r_off, c_off in directions:
                new_r = r_off + r
                new_c = c_off + c
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if grid[new_r][new_c] == '1' and (new_r, new_c) not in visited:
                        dfs(new_r, new_c)
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    dfs(i, j)

        return count
        