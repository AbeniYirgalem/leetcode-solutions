# Find All Anagrams in a String

## Difficulty

Medium

## Problem Description

Given strings s and p, return all start indices of p's anagrams in s.

## Constraints

- 1 <= s.length, p.length <= 3 \* 10^4
- s and p consist of lowercase English letters

## Example Input/Output

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

## Step-by-Step Explanation

1. Count character frequencies of p.
2. Slide a window of length p over s.
3. Record indices when counts match.

## Optimized Approach

Fixed-size sliding window with 26 counts.

## Time Complexity

O(n)

## Space Complexity

O(1)
