from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets: List[float] = []

        for pos, spd in cars:
            time = (target - pos) / spd
            if not fleets or time > fleets[-1]:
                fleets.append(time)

        return len(fleets)


if __name__ == "__main__":
    sol = Solution()
    print(sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print(sol.carFleet(10, [3], [3]))
    print(sol.carFleet(100, [0, 2, 4], [4, 2, 1]))
