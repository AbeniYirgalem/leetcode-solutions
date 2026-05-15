from collections import deque


class RecentCounter:
    def __init__(self) -> None:
        self.calls = deque()

    def ping(self, t: int) -> int:
        self.calls.append(t)
        while self.calls and self.calls[0] < t - 3000:
            self.calls.popleft()
        return len(self.calls)

if __name__ == "__main__":
    counter = RecentCounter()
    print(counter.ping(1))
    print(counter.ping(3001))
