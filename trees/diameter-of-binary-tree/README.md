# Diameter of Binary Tree

## Difficulty

Easy

## Problem Description

Return the length of the diameter of a binary tree, which is the number of edges on the longest path between any two nodes.

## Constraints

- The number of nodes is in the range [0, 10^4]
- -100 <= Node.val <= 100

## Example Input/Output

Input: root = [1,2,3,4,5]
Output: 3

## Step-by-Step Explanation

1. Compute the height of each subtree.
2. The diameter through a node is left height + right height.
3. Track the maximum across all nodes.

## Optimized Approach

Single DFS that returns height and updates a global maximum.

## Time Complexity

O(n)

## Space Complexity

O(h)
