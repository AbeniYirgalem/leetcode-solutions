# Number of Recent Calls

**Difficulty:** Easy

## Problem Description

You have a class that receives a stream of timestamps (in milliseconds). For each ping(t), return the number of calls in the last 3000 milliseconds, inclusive.

## Examples

**Input:** pings = [1, 100, 3001, 3002]
**Output:** [1, 2, 3, 3]

**Input:** pings = [10, 20, 30, 3010]
**Output:** [1, 2, 3, 3]

## Step-by-Step Approach

1. Store all timestamps in a queue.
2. On each ping, push the timestamp.
3. Pop from the front while timestamps are older than t - 3000.
4. The queue size is the answer.

## Time and Space Complexity

- **Time:** O(1) amortized per ping
- **Space:** O(n)
