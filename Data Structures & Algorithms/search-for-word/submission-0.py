class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)

        def backtrack(index, r, c):
            if index == n:
                return True
            if (r < 0 or r >= rows) or (c < 0 or c >= cols):
                return False
            if word[index] != board[r][c]:
                return False
            tmp = board[r][c]
            board[r][c] = '#'

            for r_off, c_off in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if backtrack(index + 1, r + r_off, c + c_off):
                    return True
            
            board[r][c] = tmp
            return False



        for i in range(rows):
            for j in range(cols):
                if backtrack(0,i, j):
                    return True
        return False

        