# Sliding Window Maximum

## Difficulty

Hard

## Problem Description

Given an array and a window size k, return the maximum value in each sliding window of size k.

## Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length

## Example Input/Output

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

## Step-by-Step Explanation

1. Use a deque to store indices in decreasing order of values.
2. The front of the deque is always the max for the current window.
3. Remove indices that fall out of the window.

## Optimized Approach

Monotonic deque of indices for O(1) max retrieval per step.

## Time Complexity

O(n)

## Space Complexity

O(k)
