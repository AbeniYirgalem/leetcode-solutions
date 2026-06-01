# Non-overlapping Intervals

## Difficulty

Medium

## Problem Description

Given intervals, return the minimum number of intervals you need to remove to make the rest non-overlapping.

## Constraints

- 1 <= intervals.length <= 10^5
- intervals[i].length == 2

## Example Input/Output

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1

## Step-by-Step Explanation

1. Sort intervals by end time.
2. Select the interval with the earliest end.
3. Count overlaps when the next start is before the last selected end.

## Optimized Approach

Greedy by earliest end time.

## Time Complexity

O(n log n)

## Space Complexity

O(1)
