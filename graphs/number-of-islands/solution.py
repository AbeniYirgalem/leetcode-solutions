from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    stack = [(r, c)]
                    grid[r][c] = "0"
                    while stack:
                        cr, cc = stack.pop()
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                stack.append((nr, nc))
        return count

if __name__ == "__main__":
    sol = Solution()
    grid1 = [
        ["1", "1", "0", "0"],
        ["1", "1", "0", "0"],
        ["0", "0", "1", "0"],
        ["0", "0", "0", "1"],
    ]
    grid2 = [["0", "0"], ["0", "0"]]
    print(sol.numIslands(grid1))
    print(sol.numIslands(grid2))
