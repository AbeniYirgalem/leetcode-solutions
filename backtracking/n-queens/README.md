# N-Queens

## Difficulty

Hard

## Problem Description

Place n queens on an n x n chessboard so that no two queens attack each other. Return all distinct solutions.

## Constraints

- 1 <= n <= 9

## Example Input/Output

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

## Step-by-Step Explanation

1. Place queens row by row.
2. Track used columns and diagonals.
3. When a row is completed, record the board.

## Optimized Approach

Backtracking with sets for columns and diagonals.

## Time Complexity

O(n!)

## Space Complexity

O(n)
