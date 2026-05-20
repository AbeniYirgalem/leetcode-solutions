# Valid Sudoku

## Difficulty

Medium

## Problem Description

Determine if a 9x9 Sudoku board is valid. Only filled cells need to be validated.

## Constraints

- board is a 9 x 9 matrix
- board[i][j] is a digit or '.'

## Example Input/Output

Input: board = [["5","3",".",".","7",".",".",".","."], ...]
Output: true

## Step-by-Step Explanation

1. Use sets to track digits seen in each row, column, and 3x3 box.
2. If a duplicate is found, the board is invalid.

## Optimized Approach

Single pass with row, column, and box sets.

## Time Complexity

O(81)

## Space Complexity

O(81)
