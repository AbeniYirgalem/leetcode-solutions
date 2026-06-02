# Copy List with Random Pointer

## Difficulty

Medium

## Problem Description

Each node has a next pointer and a random pointer that can point to any node or null. Return a deep copy of the list.

## Constraints

- The number of nodes is in the range [0, 1000]
- -10^4 <= Node.val <= 10^4

## Example Input/Output

Input: head = [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
Output: deep copy with the same structure

## Step-by-Step Explanation

1. Create a mapping from original nodes to their clones.
2. In a second pass, connect next and random pointers using the map.

## Optimized Approach

Use a hash map for O(1) access to cloned nodes.

## Time Complexity

O(n)

## Space Complexity

O(n)
