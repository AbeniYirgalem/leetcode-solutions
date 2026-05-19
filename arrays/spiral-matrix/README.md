# Spiral Matrix

## Difficulty

Medium

## Problem Description

Given an m x n matrix, return all elements in spiral order.

## Constraints

- 1 <= m, n <= 100
- -100 <= matrix[i][j] <= 100

## Example Input/Output

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

## Step-by-Step Explanation

1. Maintain four boundaries: top, bottom, left, right.
2. Traverse right, down, left, and up while shrinking boundaries.
3. Stop when boundaries cross.

## Optimized Approach

Boundary simulation in O(m\*n).

## Time Complexity

O(m\*n)

## Space Complexity

O(1) extra (excluding output)
