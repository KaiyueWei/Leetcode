class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_queue = deque()
        p_seen = set()
        a_queue = deque()
        a_seen = set()
        rows = len(heights)
        cols = len(heights[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        #pacific 
        #row = 0
        for i in range(cols):
            p_queue.append((0, i))
            p_seen.add((0, i))
        #col = 0
        for j in range(1, rows):
            p_queue.append((j, 0))
            p_seen.add((j, 0))
        
        #atlantic
        #row = rows - 1
        for i in range(cols):
            a_queue.append((rows-1, i))
            a_seen.add((rows-1, i))
        #col = cols - 1
        for j in range(0, rows-1):
            a_queue.append((j, cols-1))
            a_seen.add((j, cols-1))
        

        def bfs(queue, seen):
            res = set()
            while queue:
                cur = queue.popleft()
                res.add(cur)
                r, c = cur
                for r_off, c_off in directions:
                    new_c = c + c_off
                    new_r = r + r_off
                    if 0 <= new_c < cols and 0 <= new_r < rows and \
                    heights[new_r][new_c] >= heights[r][c] and (new_r, new_c) not in seen:
                        queue.append((new_r, new_c))
                        seen.add((new_r, new_c))
            return res

        p_res = bfs(p_queue, p_seen)
        a_res = bfs(a_queue,a_seen)
    
        return list(p_res & a_res)



        