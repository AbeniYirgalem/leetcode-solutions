# Search a 2D Matrix

## Difficulty

Medium

## Problem Description

Given an m x n matrix where each row is sorted and the first element of each row is greater than the last element of the previous row, determine if a target value exists.

## Constraints

- 1 <= m, n <= 100
- -10^4 <= matrix[i][j] <= 10^4
- -10^4 <= target <= 10^4

## Example Input/Output

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

## Step-by-Step Explanation

1. Treat the matrix as a sorted 1D array of length m\*n.
2. Perform binary search using index mapping: value at index i is matrix[i // n][i % n].

## Optimized Approach

Binary search on the virtual 1D array.

## Time Complexity

O(log(m\*n))

## Space Complexity

O(1)
