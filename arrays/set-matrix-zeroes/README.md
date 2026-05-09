# Set Matrix Zeroes

**Difficulty:** Medium

## Problem Description

Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

## Examples

**Input:** matrix = [[1,1,1],[1,0,1],[1,1,1]]
**Output:** [[1,0,1],[0,0,0],[1,0,1]]

**Input:** matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
**Output:** [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

## Step-by-Step Approach

1. Use the first row and first column as markers for zeroed rows/cols.
2. Track whether the first row/column should be zeroed separately.
3. Zero out cells based on markers, then handle the first row/column.

## Time and Space Complexity

- **Time:** O(m \* n)
- **Space:** O(1)
