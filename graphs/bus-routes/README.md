# Bus Routes

## Difficulty

Hard

## Problem Description

Given bus routes, return the minimum number of buses needed to travel from source to target. Return -1 if impossible.

## Constraints

- 1 <= routes.length <= 500
- 1 <= routes[i].length <= 10^5
- 0 <= source, target <= 10^6

## Example Input/Output

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2

## Step-by-Step Explanation

1. Build a map from stop to routes that include it.
2. BFS over routes, not stops.
3. Count the number of bus transfers.

## Optimized Approach

BFS over routes with stop-to-route mapping.

## Time Complexity

O(total stops)

## Space Complexity

O(total stops)
