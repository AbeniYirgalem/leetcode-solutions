# Linked List Cycle

## Difficulty

Easy

## Problem Description

Given the head of a linked list, determine if the list has a cycle.

## Constraints

- The number of nodes is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the list

## Example Input/Output

Input: head = [3, 2, 0, -4], pos = 1
Output: true

## Step-by-Step Explanation

1. Use two pointers: slow moves one step, fast moves two steps.
2. If there is a cycle, the pointers will meet.
3. If fast reaches the end, there is no cycle.

## Optimized Approach

Floyd's cycle detection (tortoise and hare).

## Time Complexity

O(n)

## Space Complexity

O(1)
