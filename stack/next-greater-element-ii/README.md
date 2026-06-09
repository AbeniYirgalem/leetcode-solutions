# Next Greater Element II

## Difficulty

Medium

## Problem Description

Given a circular array, for each element find the next greater element while moving to the right and wrapping around once. If none exists, return -1 for that position.

## Constraints

- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9

## Example Input/Output

Input: nums = [1, 2, 1]
Output: [2, -1, 2]

## Step-by-Step Explanation

1. Traverse the array twice to simulate circular behavior.
2. Use a decreasing stack of indices.
3. When a larger value appears, it is the next greater for indices in the stack.

## Optimized Approach

Iterate 2n positions with modulo indexing and a monotonic stack. Push indices only from the first pass.

## Time Complexity

O(n)

## Space Complexity

O(n)
