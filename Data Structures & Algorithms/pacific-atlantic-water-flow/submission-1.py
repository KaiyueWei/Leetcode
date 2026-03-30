class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        p_que = deque()
        p_seen = set()
        a_que = deque()
        a_seen = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        #pacific
        #row = 0
        for j in range(cols):
            p_que.append((0, j))
            p_seen.add((0, j))
        #col = 0
        for i in range(1, rows):
            p_que.append((i, 0))
            p_seen.add((i, 0))
        
        #atlantic
        #row = rows - 1
        for j in range(cols):
            a_que.append((rows-1, j))
            a_seen.add((rows-1, j))
        #col = cols - 1
        for i in range(rows - 1):
            a_que.append((i, cols - 1))
            a_seen.add((i, cols - 1))

        def get_coords(que, seen):
            coords = set()
            while que:
                i, j = que.popleft()
                coords.add((i, j))
                for i_off, j_off in directions:
                    r, c = i + i_off, j + j_off
                    if 0 <= r < rows and 0 <= c < cols and heights[r][c] >= heights[i][j] and (r, c) not in seen:
                        seen.add((r, c))
                        que.append((r, c))
            return coords

        p_coords = get_coords(p_que, p_seen)
        a_coords = get_coords(a_que, a_seen)

        return list(p_coords.intersection(a_coords))              