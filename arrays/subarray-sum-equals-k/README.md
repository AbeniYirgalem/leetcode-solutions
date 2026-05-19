# Subarray Sum Equals K

## Difficulty

Medium

## Problem Description

Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.

## Constraints

- 1 <= nums.length <= 2 \* 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

## Example Input/Output

Input: nums = [1,1,1], k = 2
Output: 2

## Step-by-Step Explanation

1. Use a running prefix sum.
2. If current_sum - k appeared before, those prefixes form valid subarrays.
3. Track counts in a hashmap.

## Optimized Approach

Prefix sum frequency map.

## Time Complexity

O(n)

## Space Complexity

O(n)
