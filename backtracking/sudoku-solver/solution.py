from typing import List, Tuple


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties: List[Tuple[int, int]] = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(i: int) -> bool:
            if i == len(empties):
                return True
            r, c = empties[i]
            box = (r // 3) * 3 + (c // 3)
            for d in "123456789":
                if d in rows[r] or d in cols[c] or d in boxes[box]:
                    continue
                board[r][c] = d
                rows[r].add(d)
                cols[c].add(d)
                boxes[box].add(d)
                if backtrack(i + 1):
                    return True
                board[r][c] = "."
                rows[r].remove(d)
                cols[c].remove(d)
                boxes[box].remove(d)
            return False

        backtrack(0)


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    sol.solveSudoku(board)
    print(board)
    board2 = [["."] * 9 for _ in range(9)]
    sol.solveSudoku(board2)
    print(board2[0][0])
    board3 = [list("534678912"), list("672195348"), list("198342567"), list("859761423"), list("426853791"), list("713924856"), list("961537284"), list("287419635"), list("345286179")]
    sol.solveSudoku(board3)
    print(board3[0][0])
