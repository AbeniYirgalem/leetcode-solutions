# Evaluate Reverse Polish Notation

## Difficulty

Medium

## Problem Description

Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, \*, /. Division should truncate toward zero.

## Constraints

- 1 <= tokens.length <= 10^4
- tokens[i] is an operator or an integer in the range [-200, 200]

## Example Input/Output

Input: tokens = ["2", "1", "+", "3", "*"]
Output: 9

## Step-by-Step Explanation

1. Scan tokens from left to right.
2. Push numbers onto a stack.
3. When an operator appears, pop two numbers, apply the operator, and push the result.

## Optimized Approach

Use a stack to evaluate the expression in one pass.

## Time Complexity

O(n)

## Space Complexity

O(n)
