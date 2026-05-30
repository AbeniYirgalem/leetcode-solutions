from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        in_mst = [False] * n
        min_dist = [float("inf")] * n
        min_dist[0] = 0
        total = 0

        for _ in range(n):
            u = -1
            for i in range(n):
                if not in_mst[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i
            in_mst[u] = True
            total += min_dist[u]
            for v in range(n):
                if not in_mst[v]:
                    cost = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if cost < min_dist[v]:
                        min_dist[v] = cost
        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
    print(sol.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))
    print(sol.minCostConnectPoints([[0, 0]]))
