from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            state, steps = queue.popleft()
            if state == target:
                return steps
            for i in range(4):
                digit = int(state[i])
                for diff in (-1, 1):
                    new_digit = (digit + diff) % 10
                    next_state = state[:i] + str(new_digit) + state[i + 1 :]
                    if next_state not in dead and next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, steps + 1))
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
    print(sol.openLock(["8888"], "0009"))
    print(sol.openLock(["0000"], "8888"))
