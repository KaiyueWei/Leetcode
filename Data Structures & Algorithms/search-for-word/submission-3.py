class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        len_w = len(word)

        def backtrack(index, r, c):
            ## stop
            if index == len_w:
                return True
            ## out of bounds
            if (r < 0 or r >= rows) or \
                (c < 0 or c >= cols):
                return False
            ## fails
            if board[r][c] != word[index]:
                return False
            
            tmp = board[r][c]
            board[r][c] = '#'
            for r_off, c_off in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r = r_off + r
                new_c = c_off + c
                if backtrack(index+1, new_r, new_c):
                    return True
            board[r][c] = tmp
            return False
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(0, i, j):
                    return True
        
        return False
        