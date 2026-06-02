# Remove Nth Node From End of List

## Difficulty

Medium

## Problem Description

Given the head of a linked list, remove the nth node from the end and return the head.

## Constraints

- The number of nodes is in the range [1, 30]
- 0 <= Node.val <= 100
- 1 <= n <= size of list

## Example Input/Output

Input: head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]

## Step-by-Step Explanation

1. Use a dummy node to simplify edge cases.
2. Move a fast pointer n steps ahead.
3. Move fast and slow together until fast reaches the end.
4. Remove the node after slow.

## Optimized Approach

Two-pointer technique with a single pass through the list.

## Time Complexity

O(n)

## Space Complexity

O(1)
