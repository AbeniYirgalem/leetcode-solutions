# Task Scheduler

## Difficulty

Medium

## Problem Description

Given tasks represented by letters and a cooldown n, return the minimum intervals needed to finish all tasks.

## Constraints

- 1 <= tasks.length <= 10^4
- tasks[i] is an uppercase English letter
- 0 <= n <= 100

## Example Input/Output

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8

## Step-by-Step Explanation

1. Count the frequency of each task.
2. The most frequent task determines the schedule frame.
3. Fill idle slots with other tasks; result is max of formula and task count.

## Optimized Approach

Use a counting-based formula without simulation.

## Time Complexity

O(t) where t is number of tasks

## Space Complexity

O(1)
