# Continuous Subarray Sum

## Difficulty

Medium

## Problem Description

Given an array of integers and an integer k, determine if the array has a continuous subarray of size at least 2 whose sum is a multiple of k.

## Constraints

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- -10^9 <= k <= 10^9

## Example Input/Output

Input: nums = [23,2,4,6,7], k = 6
Output: true

## Step-by-Step Explanation

1. Use prefix sums modulo k.
2. If the same remainder appears again with distance >= 2, the subarray sum is divisible by k.
3. Handle k = 0 by checking for consecutive zeros.

## Optimized Approach

Hashmap of first index for each remainder.

## Time Complexity

O(n)

## Space Complexity

O(min(n, k))
