class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0

        def visit(r, c):
            visited.add((r, c))
            for r_off, c_off in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_r, new_c = r+r_off, c+c_off
                if (0 <= new_r < rows) and (0 <= new_c < cols):
                    if grid[new_r][new_c] == '1' and (new_r, new_c) not in visited:
                        visit(new_r, new_c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    visit(r, c)
                    count += 1
        return count
        


            
        