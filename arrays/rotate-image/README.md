# Rotate Image

## Difficulty

Medium

## Problem Description

Rotate an n x n matrix 90 degrees clockwise in-place.

## Constraints

- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

## Example Input/Output

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

## Step-by-Step Explanation

1. Transpose the matrix (swap across the diagonal).
2. Reverse each row to complete the rotation.

## Optimized Approach

In-place transpose and row reversal.

## Time Complexity

O(n^2)

## Space Complexity

O(1)
