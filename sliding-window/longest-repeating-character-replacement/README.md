# Longest Repeating Character Replacement

## Difficulty

Medium

## Problem Description

Given a string s and an integer k, return the length of the longest substring where you can replace at most k characters to make all characters the same.

## Constraints

- 1 <= s.length <= 10^5
- 0 <= k <= s.length
- s consists of uppercase English letters

## Example Input/Output

Input: s = "AABABBA", k = 1
Output: 4

## Step-by-Step Explanation

1. Use a sliding window with character counts.
2. Track the count of the most frequent character in the window.
3. Shrink the window when replacements exceed k.

## Optimized Approach

Sliding window with max frequency tracking.

## Time Complexity

O(n)

## Space Complexity

O(1)
