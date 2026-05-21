# Restore IP Addresses

## Difficulty

Medium

## Problem Description

Given a string containing only digits, return all possible valid IP address combinations.

## Constraints

- 1 <= s.length <= 20
- s contains only digits

## Example Input/Output

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

## Step-by-Step Explanation

1. Split the string into 4 parts.
2. Each part must be 0-255 and no leading zeros.
3. Backtrack through possible segment lengths.

## Optimized Approach

Backtracking with pruning by remaining length.

## Time Complexity

O(1) bounded by 3^4

## Space Complexity

O(1) extra besides output
