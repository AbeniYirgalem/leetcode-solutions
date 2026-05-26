from typing import List, Dict, Tuple
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        distances = {i: float("inf") for i in range(1, n + 1)}
        distances[k] = 0
        heap = [(0, k)]

        while heap:
            dist, node = heapq.heappop(heap)
            if dist > distances[node]:
                continue
            for neighbor, weight in graph[node]:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        max_dist = max(distances.values())
        return -1 if max_dist == float("inf") else int(max_dist)


if __name__ == "__main__":
    sol = Solution()
    print(sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
    print(sol.networkDelayTime([[1, 2, 1]], 2, 1))
    print(sol.networkDelayTime([[1, 2, 1]], 2, 2))
