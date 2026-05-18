from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()


if __name__ == "__main__":
    sol = Solution()
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(matrix1)
    print(matrix1)
    matrix2 = [[5, 1], [2, 4]]
    sol.rotate(matrix2)
    print(matrix2)
    matrix3 = [[1]]
    sol.rotate(matrix3)
    print(matrix3)
