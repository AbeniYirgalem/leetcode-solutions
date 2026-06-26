# Invert Binary Tree

## Difficulty

Easy

## Problem Description

Invert a binary tree by swapping the left and right child of every node.

## Constraints

- The number of nodes is in the range [0, 100]
- -100 <= Node.val <= 100

## Example Input/Output

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

## Step-by-Step Explanation

1. Recursively invert left and right subtrees.
2. Swap the left and right children.

## Optimized Approach

Simple DFS recursion.

## Time Complexity

O(n)

## Space Complexity

O(h)
