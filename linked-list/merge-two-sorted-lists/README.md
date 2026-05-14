# Merge Two Sorted Lists

**Difficulty:** Easy

## Problem Description

Given the heads of two sorted linked lists, merge them into one sorted linked list and return its head.

## Examples

**Input:** list1 = [1,2,4], list2 = [1,3,4]
**Output:** [1,1,2,3,4,4]

**Input:** list1 = [], list2 = []
**Output:** []

## Step-by-Step Approach

1. Create a dummy head to simplify edge cases.
2. Use a pointer to build the merged list by always selecting the smaller current node.
3. When one list ends, append the remaining nodes of the other list.

## Time and Space Complexity

- **Time:** O(n + m)
- **Space:** O(1) extra space
