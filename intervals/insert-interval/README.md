# Insert Interval

## Difficulty

Medium

## Problem Description

Given a list of non-overlapping intervals sorted by start time and a new interval, insert the new interval and merge if necessary.

## Constraints

- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- intervals is sorted by start

## Example Input/Output

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

## Step-by-Step Explanation

1. Add all intervals ending before the new interval starts.
2. Merge overlapping intervals with the new interval.
3. Add remaining intervals.

## Optimized Approach

Single pass with merge logic.

## Time Complexity

O(n)

## Space Complexity

O(n)
