from typing import List, Dict
import heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph: Dict[str, List[str]] = {}
        for src, dst in tickets:
            graph.setdefault(src, []).append(dst)
        for src in graph:
            heapq.heapify(graph[src])

        route: List[str] = []

        def dfs(airport: str) -> None:
            heap = graph.get(airport, [])
            while heap:
                dfs(heapq.heappop(heap))
            route.append(airport)

        dfs("JFK")
        return route[::-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(sol.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
    print(sol.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
