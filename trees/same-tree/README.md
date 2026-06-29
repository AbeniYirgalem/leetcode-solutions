# Same Tree

## Difficulty

Easy

## Problem Description

Given two binary trees, determine if they are the same. Two trees are the same if they have the same structure and node values.

## Constraints

- The number of nodes is in the range [0, 100]
- -10^4 <= Node.val <= 10^4

## Example Input/Output

Input: p = [1,2,3], q = [1,2,3]
Output: true

## Step-by-Step Explanation

1. Compare nodes recursively.
2. If both are null, they match.
3. If values differ or structure differs, return false.

## Optimized Approach

Recursive DFS comparison.

## Time Complexity

O(n)

## Space Complexity

O(h)
