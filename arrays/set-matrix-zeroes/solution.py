from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
        first_col_zero = any(matrix[r][0] == 0 for r in range(rows))
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0

if __name__ == "__main__":
    sol = Solution()
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroes(matrix1)
    print(matrix1)
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol.setZeroes(matrix2)
    print(matrix2)
