# Pacific Atlantic Water Flow

## Difficulty

Medium

## Problem Description

Given a matrix of heights, water can flow from a cell to another if the next cell has height less than or equal. Return all coordinates that can reach both the Pacific and Atlantic oceans.

## Constraints

- 1 <= m, n <= 200
- 0 <= heights[i][j] <= 10^5

## Example Input/Output

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

## Step-by-Step Explanation

1. Start from the Pacific borders and mark all cells that can reach the Pacific.
2. Start from the Atlantic borders and mark all cells that can reach the Atlantic.
3. A cell is valid if it appears in both reachable sets.

## Optimized Approach

Reverse the flow: move from the oceans inward using non-decreasing heights.

## Time Complexity

O(m\*n)

## Space Complexity

O(m\*n)
