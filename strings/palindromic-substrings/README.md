# Palindromic Substrings

## Difficulty

Medium

## Problem Description

Given a string, count how many substrings are palindromic.

## Constraints

- 1 <= s.length <= 1000
- s consists of lowercase English letters

## Example Input/Output

Input: s = "aaa"
Output: 6

## Step-by-Step Explanation

1. Each character and gap between characters can be a palindrome center.
2. Expand around every center and count valid palindromes.

## Optimized Approach

Expand around center for all 2n-1 centers.

## Time Complexity

O(n^2)

## Space Complexity

O(1)
