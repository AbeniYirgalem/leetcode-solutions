# Reorder List

## Difficulty

Medium

## Problem Description

Given the head of a singly linked list, reorder it as L0 -> Ln -> L1 -> Ln-1 -> ... without changing node values.

## Constraints

- The number of nodes is in the range [1, 5 * 10^4]
- -10^5 <= Node.val <= 10^5

## Example Input/Output

Input: head = [1, 2, 3, 4]
Output: [1, 4, 2, 3]

## Step-by-Step Explanation

1. Find the middle of the list.
2. Reverse the second half.
3. Merge the two halves by alternating nodes.

## Optimized Approach

Use slow and fast pointers for the middle, reverse in-place, then weave.

## Time Complexity

O(n)

## Space Complexity

O(1)
