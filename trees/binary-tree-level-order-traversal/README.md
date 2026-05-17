# Binary Tree Level Order Traversal

**Difficulty:** Medium

## Problem Description

Given the root of a binary tree, return the level order traversal of its node values.

## Examples

**Input:** root = [3,9,20,null,null,15,7]
**Output:** [[3],[9,20],[15,7]]

**Input:** root = []
**Output:** []

## Step-by-Step Approach

1. Use a queue to process nodes level by level.
2. For each level, pop all nodes currently in the queue.
3. Add their children to the queue and record values for the level.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(n)
