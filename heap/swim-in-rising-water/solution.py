from typing import List, Tuple
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap: List[Tuple[int, int, int]] = [(grid[0][0], 0, 0)]
        visited = set()

        while heap:
            time, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == n - 1 and c == n - 1:
                return time
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    heapq.heappush(heap, (max(time, grid[nr][nc]), nr, nc))
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.swimInWater([[0, 2], [1, 3]]))
    print(sol.swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))
    print(sol.swimInWater([[0]]))
