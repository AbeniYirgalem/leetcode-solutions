# Remove Invalid Parentheses

## Difficulty

Hard

## Problem Description

Remove the minimum number of invalid parentheses to make the input string valid. Return all possible results.

## Constraints

- 1 <= s.length <= 25
- s consists of parentheses and lowercase letters

## Example Input/Output

Input: s = "()())()"
Output: ["(())()","()()()"]

## Step-by-Step Explanation

1. Use BFS to explore strings with minimal removals.
2. Stop after the first valid level is found.
3. Collect all valid strings at that level.

## Optimized Approach

Breadth-first search with pruning by visited set.

## Time Complexity

O(2^n)

## Space Complexity

O(2^n)
