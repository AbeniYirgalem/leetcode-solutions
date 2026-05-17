# Kth Smallest Element in a BST

**Difficulty:** Medium

## Problem Description

Given the root of a BST and an integer k, return the k-th smallest value.

## Examples

**Input:** root = [3,1,4,null,2], k = 1
**Output:** 1

**Input:** root = [5,3,6,2,4,null,null,1], k = 3
**Output:** 3

## Step-by-Step Approach

1. Inorder traversal of a BST yields sorted values.
2. Traverse inorder and count nodes until k is reached.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(h)
