from typing import List, Tuple


class MinStack:
    def __init__(self) -> None:
        self.stack: List[Tuple[int, int]] = []

    def push(self, val: int) -> None:
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(3)
    min_stack.push(5)
    print(min_stack.getMin())
    min_stack.push(2)
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.top())
