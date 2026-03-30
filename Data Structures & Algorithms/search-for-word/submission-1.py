class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)

        def backtrack(index, r, c):
            #goal
            if index == n:
                return True
            #boudary
            if (r < 0 or r >= rows) or (c < 0 or c >= cols):
                return False
            #fail the goal
            if word[index] != board[r][c]:
                return False
            #mark the current char as visited
            tmp = board[r][c]
            board[r][c] = '#'
            #choices
            for r_off, c_off in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if backtrack(index + 1, r + r_off, c + c_off):
                    return True
            # if fails, backtrack
            board[r][c] = tmp
            return False

        for i in range(rows):
            for j in range(cols):
                if backtrack(0,i, j):
                    return True
        return False

        