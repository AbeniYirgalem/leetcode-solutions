from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> bool:
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return False
            if rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
            elif rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            else:
                parent[root_b] = root_a
                rank[root_a] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
    print(sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
    print(sol.validTree(1, []))
