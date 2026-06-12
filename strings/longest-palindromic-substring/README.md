# Longest Palindromic Substring

## Difficulty

Medium

## Problem Description

Given a string s, return the longest palindromic substring.

## Constraints

- 1 <= s.length <= 1000
- s consists of letters and digits

## Example Input/Output

Input: s = "babad"
Output: "bab" ("aba" is also valid)

## Step-by-Step Explanation

1. Treat every index and gap between indices as a center.
2. Expand outward while the characters match.
3. Track the longest substring found.

## Optimized Approach

Expand around center with O(1) extra space.

## Time Complexity

O(n^2)

## Space Complexity

O(1)
