# Validate Binary Search Tree

**Difficulty:** Medium

## Problem Description

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

## Examples

**Input:** root = [2,1,3]
**Output:** true

**Input:** root = [5,1,4,null,null,3,6]
**Output:** false

## Step-by-Step Approach

1. Use DFS with lower and upper bounds.
2. Each node must be strictly between its bounds.
3. Recurse to children with updated bounds.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(n)
