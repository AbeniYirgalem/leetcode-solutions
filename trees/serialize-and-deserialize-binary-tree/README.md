# Serialize and Deserialize Binary Tree

## Difficulty

Hard

## Problem Description

Design an algorithm to serialize and deserialize a binary tree. Serialization is a string representation and deserialization rebuilds the tree.

## Constraints

- The number of nodes is in the range [0, 10^4]
- -1000 <= Node.val <= 1000

## Example Input/Output

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

## Step-by-Step Explanation

1. Serialize using BFS with null markers.
2. Deserialize by reading values in order and rebuilding children.

## Optimized Approach

Breadth-first traversal keeps structure intact.

## Time Complexity

O(n)

## Space Complexity

O(n)
