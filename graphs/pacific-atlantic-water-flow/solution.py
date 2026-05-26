from typing import List, Set, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])

        def dfs(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            seen: Set[Tuple[int, int]] = set()
            stack = starts[:]
            for cell in stack:
                seen.add(cell)
            while stack:
                r, c = stack.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if (nr, nc) in seen:
                            continue
                        if heights[nr][nc] >= heights[r][c]:
                            seen.add((nr, nc))
                            stack.append((nr, nc))
            return seen

        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        pacific = dfs(pacific_starts)
        atlantic = dfs(atlantic_starts)

        result = [[r, c] for (r, c) in pacific & atlantic]
        return result


if __name__ == "__main__":
    sol = Solution()
    heights1 = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    print(sorted(sol.pacificAtlantic(heights1)))
    print(sorted(sol.pacificAtlantic([[1]])))
    print(sorted(sol.pacificAtlantic([[1, 2], [4, 3]])))
