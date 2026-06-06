# Daily Temperatures

## Difficulty

Medium

## Problem Description

Given a list of daily temperatures, return an array where each position tells you how many days you must wait to get a warmer temperature. If no warmer day exists, put 0 for that day.

## Constraints

- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

## Example Input/Output

Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]

## Step-by-Step Explanation

1. Walk through the temperatures from left to right.
2. Keep indices of days in a decreasing stack (temperatures strictly drop as you go down the stack).
3. When a warmer temperature appears, pop indices until the stack top is warmer than the current day.
4. For each popped index, the wait time is the current index minus the popped index.

## Optimized Approach

Use a monotonic decreasing stack of indices. Each index is pushed once and popped once, giving linear time.

## Time Complexity

O(n)

## Space Complexity

O(n)
