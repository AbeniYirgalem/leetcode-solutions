# Generate Parentheses

## Difficulty

Medium

## Problem Description

Given n pairs of parentheses, generate all combinations of well-formed parentheses.

## Constraints

- 1 <= n <= 8

## Example Input/Output

Input: n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

## Step-by-Step Explanation

1. Build the string step by step.
2. You can add "(" if you still have remaining left parentheses.
3. You can add ")" if it will not make the string invalid.

## Optimized Approach

Use backtracking with counts of open and closed parentheses to generate only valid states.

## Time Complexity

O(4^n / sqrt(n))

## Space Complexity

O(n)
