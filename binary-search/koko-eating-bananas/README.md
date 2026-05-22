# Koko Eating Bananas

## Difficulty

Medium

## Problem Description

Given piles of bananas and hours h, find the minimum integer eating speed k such that Koko can finish all bananas within h hours.

## Constraints

- 1 <= piles.length <= 10^4
- 1 <= piles[i] <= 10^9
- 1 <= h <= 10^9

## Example Input/Output

Input: piles = [3, 6, 7, 11], h = 8
Output: 4

## Step-by-Step Explanation

1. The speed k is between 1 and max(piles).
2. For a given k, compute total hours needed by summing ceil(pile / k).
3. Use binary search to find the minimum k that fits in h.

## Optimized Approach

Binary search over the speed range.

## Time Complexity

O(n log m) where m is max pile size

## Space Complexity

O(1)
