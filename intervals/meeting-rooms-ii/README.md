# Meeting Rooms II

## Difficulty

Medium

## Problem Description

Given meeting intervals, return the minimum number of conference rooms required.

## Constraints

- 1 <= intervals.length <= 10^4
- intervals[i].length == 2

## Example Input/Output

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

## Step-by-Step Explanation

1. Sort intervals by start.
2. Use a min-heap of end times.
3. Reuse a room if the earliest end is <= current start.

## Optimized Approach

Min-heap of active meeting end times.

## Time Complexity

O(n log n)

## Space Complexity

O(n)
