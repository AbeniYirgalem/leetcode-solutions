from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float("inf")] * n
        costs[src] = 0

        for _ in range(k + 1):
            next_costs = costs[:]
            for u, v, w in flights:
                if costs[u] != float("inf") and costs[u] + w < next_costs[v]:
                    next_costs[v] = costs[u] + w
            costs = next_costs

        return -1 if costs[dst] == float("inf") else int(costs[dst])


if __name__ == "__main__":
    sol = Solution()
    print(sol.findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 3, 100], [0, 3, 500]], 0, 3, 1))
    print(sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
    print(sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100]], 0, 2, 0))
