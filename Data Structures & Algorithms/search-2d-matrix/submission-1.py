class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        ## check which row the target is located
        t = 0
        b = n - 1
        middle = (n-1) // 2
        while t <= b:
            middle = t + ((b-t)//2)
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                break 
            elif matrix[middle][0] < target:
                t = middle + 1
            elif matrix[middle][0] > target:
                b = middle - 1
            else:
                return True
        ## if there is row, check which column the target is located
        l, r = 0, m - 1
        while l <= r:
            mi = l + (r-l)//2
            if matrix[middle][mi] < target:
                l = mi + 1
            elif matrix[middle][mi] > target:
                r = mi - 1
            else:
                return True
        return False
        