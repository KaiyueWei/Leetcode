class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        rowZero = False
        colZero = False

        # First pass: mark zeros
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0:
                        rowZero = True
                    if j == 0:
                        colZero = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Zero columns based on first row
        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(1, n):
                    matrix[i][j] = 0

        # Zero rows based on first column
        for i in range(1, n):
            if matrix[i][0] == 0:
                for j in range(1, m):
                    matrix[i][j] = 0

        # Handle first row
        if rowZero:
            for j in range(m):
                matrix[0][j] = 0

        # Handle first column
        if colZero:
            for i in range(n):
                matrix[i][0] = 0