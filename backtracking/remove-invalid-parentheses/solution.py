from typing import List
from collections import deque


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(expr: str) -> bool:
            balance = 0
            for ch in expr:
                if ch == "(":
                    balance += 1
                elif ch == ")":
                    if balance == 0:
                        return False
                    balance -= 1
            return balance == 0

        visited = {s}
        queue = deque([s])
        result: List[str] = []
        found = False

        while queue:
            expr = queue.popleft()
            if is_valid(expr):
                result.append(expr)
                found = True
            if found:
                continue
            for i, ch in enumerate(expr):
                if ch not in "()":
                    continue
                nxt = expr[:i] + expr[i + 1 :]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeInvalidParentheses("()())()"))
    print(sol.removeInvalidParentheses("(a)())()"))
    print(sol.removeInvalidParentheses(")("))
