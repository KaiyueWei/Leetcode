class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        # Pacific
        for c in range(cols):
            dfs(0, c, pac)
        for r in range(rows):
            dfs(r, 0, pac)

        # Atlantic
        for c in range(cols):
            dfs(rows - 1, c, atl)
        for r in range(rows):
            dfs(r, cols - 1, atl)

        return list(pac & atl)


                