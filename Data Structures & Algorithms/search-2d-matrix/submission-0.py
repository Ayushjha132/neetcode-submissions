class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix and not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m*n - 1

        while l <= r:
            # treat as 1D matrix
            m = l + (r-l)//2
            # converting back to 2D matrix
            row = m // n
            col = m % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else: 
                r = m - 1
        return False

