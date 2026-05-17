# Binary Tree Inorder Traversal

**Difficulty:** Easy

## Problem Description

Given the root of a binary tree, return the inorder traversal of its nodes' values.

## Examples

**Input:** root = [1,null,2,3]
**Output:** [1,3,2]

**Input:** root = []
**Output:** []

## Step-by-Step Approach

1. Use an explicit stack to simulate recursion.
2. Traverse left, visit node, then traverse right.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(n)
