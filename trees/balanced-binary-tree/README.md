# Balanced Binary Tree

## Difficulty

Easy

## Problem Description

Determine if a binary tree is height-balanced. A tree is balanced if the heights of left and right subtrees differ by no more than 1.

## Constraints

- The number of nodes is in the range [0, 5000]
- -10^4 <= Node.val <= 10^4

## Example Input/Output

Input: root = [3,9,20,null,null,15,7]
Output: true

## Step-by-Step Explanation

1. Compute subtree heights.
2. If a subtree is unbalanced, propagate a sentinel value.
3. The tree is balanced if no sentinel is found.

## Optimized Approach

DFS returning height or -1 if unbalanced.

## Time Complexity

O(n)

## Space Complexity

O(h)
