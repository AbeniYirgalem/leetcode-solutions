# Reverse Linked List

## Difficulty

Easy

## Problem Description

Given the head of a singly linked list, reverse the list and return the new head.

## Constraints

- The number of nodes is in the range [0, 5000]
- -5000 <= Node.val <= 5000

## Example Input/Output

Input: head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

## Step-by-Step Explanation

1. Maintain previous and current pointers.
2. Reverse the next pointer for each node.
3. Move forward until the list ends.

## Optimized Approach

Iterative pointer reversal with constant extra space.

## Time Complexity

O(n)

## Space Complexity

O(1)
