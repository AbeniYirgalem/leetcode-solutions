# Min Stack

## Difficulty

Medium

## Problem Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

## Constraints

- -2^31 <= val <= 2^31 - 1
- Methods pop, top, and getMin will always be called on non-empty stacks

## Example Input/Output

Input:
push(3), push(5), getMin(), push(2), getMin(), pop(), top()
Output:
3, 2, 5

## Step-by-Step Explanation

1. Store each value with the current minimum at the time of push.
2. The minimum is always available at the top of the stack.
3. Pop removes both the value and its stored minimum.

## Optimized Approach

Use a stack of pairs (value, current_min). This ensures all operations are O(1).

## Time Complexity

O(1) per operation

## Space Complexity

O(n)
