# Merge Intervals

## Difficulty

Medium

## Problem Description

Given a list of intervals, merge all overlapping intervals and return the merged list.

## Constraints

- 1 <= intervals.length <= 10^4
- intervals[i].length == 2

## Example Input/Output

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

## Step-by-Step Explanation

1. Sort intervals by start.
2. Extend the current interval if overlap exists.
3. Otherwise, push the current interval and start a new one.

## Optimized Approach

Sort then merge in a single pass.

## Time Complexity

O(n log n)

## Space Complexity

O(n)
