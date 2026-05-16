# Longest Substring Without Repeating Characters

**Difficulty:** Medium

## Problem Description

Given a string, return the length of the longest substring that contains no repeated characters.

## Examples

**Input:** s = "abcabcbb"
**Output:** 3

**Input:** s = "bbbbb"
**Output:** 1

## Step-by-Step Approach

1. Use a sliding window with two pointers.
2. Track the last seen index of each character.
3. When a repeated character is found, move the left pointer past its last seen position.
4. Update the maximum length as you expand the window.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(min(n, alphabet))
