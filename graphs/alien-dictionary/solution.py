from typing import List, Dict, Set
from collections import deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph: Dict[str, Set[str]] = {ch: set() for word in words for ch in word}
        indegree: Dict[str, int] = {ch: 0 for ch in graph}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        queue = deque([ch for ch in indegree if indegree[ch] == 0])
        result = []
        while queue:
            ch = queue.popleft()
            result.append(ch)
            for nxt in graph[ch]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        if len(result) != len(indegree):
            return ""
        return "".join(result)


if __name__ == "__main__":
    sol = Solution()
    print(sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
    print(sol.alienOrder(["z", "x"]))
    print(sol.alienOrder(["abc", "ab"]))
