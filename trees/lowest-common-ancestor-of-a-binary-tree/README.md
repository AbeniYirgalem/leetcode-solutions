# Lowest Common Ancestor of a Binary Tree

**Difficulty:** Medium

## Problem Description

Given a binary tree and two nodes p and q, return their lowest common ancestor.

## Examples

**Input:** root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
**Output:** 3

**Input:** root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
**Output:** 5

## Step-by-Step Approach

1. Use DFS to search for p and q.
2. If a node is either p or q, return it.
3. If both sides return non-null, the current node is the LCA.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(n)
