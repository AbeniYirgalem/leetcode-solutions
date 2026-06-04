# Permutation in String

## Difficulty

Medium

## Problem Description

Given strings s1 and s2, return true if s2 contains a permutation of s1.

## Constraints

- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters

## Example Input/Output

Input: s1 = "ab", s2 = "eidbaooo"
Output: true

## Step-by-Step Explanation

1. Count character frequencies of s1.
2. Slide a window of length len(s1) over s2.
3. If window counts match, a permutation exists.

## Optimized Approach

Fixed-size sliding window with 26 counts.

## Time Complexity

O(n)

## Space Complexity

O(1)
