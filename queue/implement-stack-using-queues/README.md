# Implement Stack using Queues

**Difficulty:** Easy

## Problem Description

Implement a LIFO stack using only queue operations. Support push, pop, top, and empty.

## Examples

**Input:** push(1), push(2), top(), pop(), empty()
**Output:** 2, 2, false

**Input:** push(3), pop(), empty()
**Output:** 3, true

## Step-by-Step Approach

1. Use a single queue.
2. On push, enqueue the element.
3. Rotate the queue so the new element is at the front.
4. Pop and top operate on the front of the queue.

## Time and Space Complexity

- **Time:** O(n) for push, O(1) for pop/top
- **Space:** O(n)
