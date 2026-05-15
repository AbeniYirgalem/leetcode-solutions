# Valid Parentheses

**Difficulty:** Easy

## Problem Description

Given a string containing only the characters ()[]{} , determine if the brackets are valid. A string is valid if every opening bracket is closed by the same type of bracket in the correct order.

## Examples

**Input:** s = "()"
**Output:** true

**Input:** s = "(]"
**Output:** false

## Step-by-Step Approach

1. Use a stack to track opening brackets.
2. When encountering a closing bracket, ensure the stack top is the matching opening bracket.
3. If there is a mismatch or the stack is empty, the string is invalid.
4. At the end, the string is valid only if the stack is empty.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(n)
