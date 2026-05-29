from typing import List, Dict


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_run: Dict[int, int] = {}
        day = 0
        for task in tasks:
            if task in last_run and day - last_run[task] <= space:
                day = last_run[task] + space + 1
            else:
                day += 1
            last_run[task] = day
        return day


if __name__ == "__main__":
    sol = Solution()
    print(sol.taskSchedulerII([1, 2, 1, 2, 3, 1], 3))
    print(sol.taskSchedulerII([5, 8, 8, 5], 2))
    print(sol.taskSchedulerII([1], 10))
