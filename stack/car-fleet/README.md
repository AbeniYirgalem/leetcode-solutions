# Car Fleet

## Difficulty

Medium

## Problem Description

Given target distance, positions, and speeds of cars, count how many fleets arrive at the target. A car fleet forms when a faster car catches up to a slower one.

## Constraints

- 1 <= position.length == speed.length <= 10^5
- 0 <= position[i] < target <= 10^6
- 1 <= speed[i] <= 10^6

## Example Input/Output

Input: target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]
Output: 3

## Step-by-Step Explanation

1. Pair each car's position and speed.
2. Sort cars by position descending (closest to target first).
3. Compute time to target for each car.
4. Use a stack of times to merge fleets.

## Optimized Approach

Process cars from closest to farthest. A new fleet forms only when its time is greater than the last fleet time.

## Time Complexity

O(n log n)

## Space Complexity

O(n)
