# Minimum Window Substring

## Difficulty

Hard

## Problem Description

Given strings s and t, return the minimum window substring of s that contains all characters of t (including duplicates).

## Constraints

- 1 <= s.length, t.length <= 10^5
- s and t consist of English letters

## Example Input/Output

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

## Step-by-Step Explanation

1. Count required characters of t.
2. Expand the right pointer to satisfy requirements.
3. Shrink from the left to minimize the window.

## Optimized Approach

Sliding window with character counts and a satisfied counter.

## Time Complexity

O(n)

## Space Complexity

O(1)
