# Add Two Numbers

**Difficulty:** Medium

## Problem Description

Two non-empty linked lists represent two non-negative integers in reverse order. Each node contains a single digit. Add the two numbers and return the sum as a linked list in the same reverse order.

## Examples

**Input:** l1 = [2,4,3], l2 = [5,6,4]
**Output:** [7,0,8]

**Input:** l1 = [0], l2 = [0]
**Output:** [0]

## Step-by-Step Approach

1. Traverse both lists simultaneously.
2. Add corresponding digits with a carry.
3. Create a new node for each digit of the result.
4. Continue until both lists and carry are exhausted.

## Time and Space Complexity

- **Time:** O(n + m)
- **Space:** O(1) extra space
