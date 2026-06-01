# Meeting Rooms

## Difficulty

Easy

## Problem Description

Given meeting time intervals, determine if a person can attend all meetings.

## Constraints

- 1 <= intervals.length <= 10^4
- intervals[i].length == 2

## Example Input/Output

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

## Step-by-Step Explanation

1. Sort intervals by start time.
2. If any interval starts before the previous one ends, return false.

## Optimized Approach

Sort and scan for overlaps.

## Time Complexity

O(n log n)

## Space Complexity

O(1)
