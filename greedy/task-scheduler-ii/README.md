# Task Scheduler II

## Difficulty

Medium

## Problem Description

Given tasks and a space value, return the minimum number of days needed to finish all tasks, where each task type must have at least space days between executions.

## Constraints

- 1 <= tasks.length <= 10^5
- 1 <= space <= 10^5
- 1 <= tasks[i] <= 10^9

## Example Input/Output

Input: tasks = [1,2,1,2,3,1], space = 3
Output: 9

## Step-by-Step Explanation

1. Track the last day each task was run.
2. If a task is scheduled too early, jump the day forward.
3. Update the last run day for each task.

## Optimized Approach

Greedy simulation with hash map.

## Time Complexity

O(n)

## Space Complexity

O(n)
