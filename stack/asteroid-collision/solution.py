from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack: List[int] = []

        for asteroid in asteroids:
            alive = True
            while alive and stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                alive = False
            if alive:
                stack.append(asteroid)

        return stack


if __name__ == "__main__":
    sol = Solution()
    print(sol.asteroidCollision([5, 10, -5]))
    print(sol.asteroidCollision([8, -8]))
    print(sol.asteroidCollision([10, 2, -5]))
