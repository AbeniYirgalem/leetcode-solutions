from typing import List, Tuple


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])

        def mark_safe(starts: List[Tuple[int, int]]) -> None:
            stack = starts
            while stack:
                r, c = stack.pop()
                if board[r][c] != "O":
                    continue
                board[r][c] = "S"
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                        stack.append((nr, nc))

        starts = []
        for c in range(cols):
            starts.append((0, c))
            starts.append((rows - 1, c))
        for r in range(rows):
            starts.append((r, 0))
            starts.append((r, cols - 1))
        mark_safe(starts)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"


if __name__ == "__main__":
    sol = Solution()
    board1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    sol.solve(board1)
    print(board1)
    board2 = [["X", "O", "X"], ["O", "O", "O"], ["X", "O", "X"]]
    sol.solve(board2)
    print(board2)
    board3 = [["O"]]
    sol.solve(board3)
    print(board3)
