# Rotting Oranges

**Difficulty:** Medium

## Problem Description

Given a grid where 0 is empty, 1 is fresh, and 2 is rotten, return the minimum minutes to rot all fresh oranges, or -1 if impossible.

## Examples

**Input:** grid = [[2,1,1],[1,1,0],[0,1,1]]
**Output:** 4

**Input:** grid = [[2,1,1],[0,1,1],[1,0,1]]
**Output:** -1

## Step-by-Step Approach

1. Add all initially rotten oranges to a queue.
2. BFS level by level to rot adjacent fresh oranges.
3. Track minutes and remaining fresh count.

## Time and Space Complexity

- **Time:** O(m \* n)
- **Space:** O(m \* n)
