from typing import Dict, List, Tuple
import bisect


class TimeMap:
    def __init__(self) -> None:
        self.store: Dict[str, List[Tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        items = self.store[key]
        idx = bisect.bisect_right(items, (timestamp, chr(127))) - 1
        if idx >= 0:
            return items[idx][1]
        return ""


if __name__ == "__main__":
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)
    print(time_map.get("foo", 1))
    print(time_map.get("foo", 3))
    time_map.set("foo", "bar2", 4)
    print(time_map.get("foo", 4))
    print(time_map.get("foo", 5))
