class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        length = len(word)

        def backtrack(index, r, c):
            ## goal
            if index == length:
                return True
            if (r < 0 or r >= rows) or (c < 0 or c >= cols):
                return False
            ## fail
            if board[r][c] != word[index]:
                return False
            
            tmp = board[r][c]
            board[r][c] = '#'
            ## choices
            for r_offset, c_offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_r = r + r_offset
                new_c = c + c_offset
                if backtrack(index + 1, new_r, new_c):
                    return True
            board[r][c] = tmp

            return False
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(0, i, j):
                    return True
        
        return False
        