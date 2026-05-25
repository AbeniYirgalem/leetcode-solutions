from typing import List, Dict
from collections import deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stop_to_routes: Dict[int, List[int]] = {}
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes.setdefault(stop, []).append(i)

        visited_routes = set()
        visited_stops = {source}
        queue = deque([(source, 0)])

        while queue:
            stop, buses = queue.popleft()
            for route_idx in stop_to_routes.get(stop, []):
                if route_idx in visited_routes:
                    continue
                visited_routes.add(route_idx)
                for next_stop in routes[route_idx]:
                    if next_stop == target:
                        return buses + 1
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses + 1))
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))
    print(sol.numBusesToDestination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12))
    print(sol.numBusesToDestination([[1, 2, 3]], 1, 3))
