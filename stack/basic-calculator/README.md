# Basic Calculator

## Difficulty

Hard

## Problem Description

Given a string s representing a valid expression with '+', '-', parentheses, and spaces, evaluate it.

## Constraints

- 1 <= s.length <= 3 \* 10^5
- s consists of digits, '+', '-', '(', ')', and spaces

## Example Input/Output

Input: s = "1 + (2 - 3) + 4"
Output: 4

## Step-by-Step Explanation

1. Use a running result and sign.
2. Push current result and sign when encountering '('.
3. Pop to combine when encountering ')'.

## Optimized Approach

Single pass with a stack for parentheses context.

## Time Complexity

O(n)

## Space Complexity

O(n)
