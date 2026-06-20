# Binary Tree Maximum Path Sum

## Difficulty

Hard

## Problem Description

Return the maximum path sum in a binary tree, where a path can start and end at any node.

## Constraints

- The number of nodes is in the range [1, 3 * 10^4]
- -1000 <= Node.val <= 1000

## Example Input/Output

Input: root = [-10,9,20,null,null,15,7]
Output: 42

## Step-by-Step Explanation

1. Compute maximum gain from each node to its parent.
2. For each node, compute path sum through both children.
3. Track the global maximum.

## Optimized Approach

DFS returning max downward path and updating global best.

## Time Complexity

O(n)

## Space Complexity

O(h)
