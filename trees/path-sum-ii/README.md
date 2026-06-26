# Path Sum II

## Difficulty

Medium

## Problem Description

Return all root-to-leaf paths where the sum of node values equals targetSum.

## Constraints

- The number of nodes is in the range [0, 5000]
- -1000 <= Node.val <= 1000

## Example Input/Output

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

## Step-by-Step Explanation

1. Use DFS to track the current path and remaining sum.
2. When at a leaf, check if the sum matches.
3. Backtrack after visiting children.

## Optimized Approach

Backtracking with path accumulation.

## Time Complexity

O(n)

## Space Complexity

O(h)
