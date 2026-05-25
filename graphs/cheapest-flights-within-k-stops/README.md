# Cheapest Flights Within K Stops

## Difficulty

Medium

## Problem Description

Find the cheapest price from src to dst with at most k stops. Return -1 if no such route exists.

## Constraints

- 1 <= n <= 100
- 0 <= flights.length <= n \* (n - 1) / 2
- 0 <= k <= n - 1
- 0 <= price <= 10^4

## Example Input/Output

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,3,100],[0,3,500]], src = 0, dst = 3, k = 1
Output: 500

## Step-by-Step Explanation

1. Use a dynamic relaxation process limited to k + 1 edges.
2. Each iteration allows one more edge than the previous.
3. Keep the best prices without using paths longer than k + 1 edges.

## Optimized Approach

Bellman-Ford variant with k + 1 relaxations.

## Time Complexity

O(k \* E)

## Space Complexity

O(V)
