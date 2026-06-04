from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        deq = deque()
        result: List[int] = []

        for i, num in enumerate(nums):
            while deq and deq[0] <= i - k:
                deq.popleft()
            while deq and nums[deq[-1]] <= num:
                deq.pop()
            deq.append(i)
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(sol.maxSlidingWindow([1], 1))
    print(sol.maxSlidingWindow([9, 11], 2))
