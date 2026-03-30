class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(pos):
            r, c = pos
            visited.add(pos)
            for r_off, c_off in directions:
                new_r = r + r_off
                new_c = c + c_off
                if 0 <= new_r < rows and 0<= new_c < cols:
                    if grid[new_r][new_c] == '1' and (new_r, new_c) not in visited:
                        dfs((new_r, new_c))
            
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs((i, j))
                    count += 1
        return count