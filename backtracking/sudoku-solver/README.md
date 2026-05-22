# Sudoku Solver

## Difficulty

Hard

## Problem Description

Solve a 9x9 Sudoku puzzle by filling empty cells. Each row, column, and 3x3 box must contain digits 1-9.

## Constraints

- board is a 9x9 grid
- Empty cells are represented by '.'

## Example Input/Output

Input: board with empty cells
Output: solved board

## Step-by-Step Explanation

1. Track used digits in rows, columns, and boxes.
2. Backtrack through empty cells.
3. Try digits and revert on failure.

## Optimized Approach

Backtracking with constraint sets to prune.

## Time Complexity

O(9^(empty)) in worst case

## Space Complexity

O(1) extra besides recursion
