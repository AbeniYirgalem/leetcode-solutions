# Implement Queue using Stacks

**Difficulty:** Easy

## Problem Description

Implement a FIFO queue using only stack operations. Support push, pop, peek, and empty.

## Examples

**Input:** push(1), push(2), peek(), pop(), empty()
**Output:** 1, 1, false

**Input:** push(3), pop(), empty()
**Output:** 3, true

## Step-by-Step Approach

1. Use two stacks: input and output.
2. Push goes to input.
3. Pop/peek pull from output; if empty, move all from input to output.

## Time and Space Complexity

- **Time:** O(1) amortized per operation
- **Space:** O(n)
