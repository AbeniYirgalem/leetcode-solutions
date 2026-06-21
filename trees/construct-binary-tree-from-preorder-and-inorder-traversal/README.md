# Construct Binary Tree from Preorder and Inorder Traversal

## Difficulty

Medium

## Problem Description

Given preorder and inorder traversal arrays of a binary tree, construct the binary tree.

## Constraints

- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- All values are unique

## Example Input/Output

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

## Step-by-Step Explanation

1. The first preorder value is the root.
2. Split inorder into left and right subtrees around the root.
3. Recursively build left and right trees.

## Optimized Approach

Use an index map to split inorder in O(1).

## Time Complexity

O(n)

## Space Complexity

O(n)
