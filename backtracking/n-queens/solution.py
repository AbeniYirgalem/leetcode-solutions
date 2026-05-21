from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c
        board = [["."] * n for _ in range(n)]
        result: List[List[str]] = []

        def backtrack(r: int) -> None:
            if r == n:
                result.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                board[r][c] = "Q"
                backtrack(r + 1)
                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(4))
    print(sol.solveNQueens(1))
    print(len(sol.solveNQueens(5)))
