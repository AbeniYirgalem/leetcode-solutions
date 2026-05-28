from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        current_tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            current_tank += diff
            if current_tank < 0:
                start = i + 1
                current_tank = 0

        return start if total_tank >= 0 else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
    print(sol.canCompleteCircuit([1], [1]))
