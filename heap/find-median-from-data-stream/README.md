# Find Median from Data Stream

## Difficulty

Hard

## Problem Description

Design a data structure that supports adding numbers and finding the median at any time.

## Constraints

- -10^5 <= num <= 10^5
- At most 5 \* 10^4 operations

## Example Input/Output

Input:
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

## Step-by-Step Explanation

1. Keep a max-heap for the lower half and a min-heap for the upper half.
2. Balance sizes so the lower half has at most one extra element.
3. Median is top of heaps depending on sizes.

## Optimized Approach

Two heaps with rebalancing.

## Time Complexity

addNum: O(log n)
findMedian: O(1)

## Space Complexity

O(n)
