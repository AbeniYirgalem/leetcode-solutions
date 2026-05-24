# Regular Expression Matching

## Difficulty

Hard

## Problem Description

Implement regular expression matching with support for '.' and '\*'. The match must cover the entire string.

## Constraints

- 0 <= s.length <= 20
- 0 <= p.length <= 30
- s contains lowercase letters
- p contains lowercase letters, '.' and '\*'

## Example Input/Output

Input: s = "aab", p = "c*a*b"
Output: true

## Step-by-Step Explanation

1. dp[i][j] indicates if s[0:i] matches p[0:j].
2. Handle '\*' by either ignoring the pair or consuming a matching character.
3. '.' matches any character.

## Optimized Approach

2D DP based on pattern rules.

## Time Complexity

O(m\*n)

## Space Complexity

O(m\*n)
