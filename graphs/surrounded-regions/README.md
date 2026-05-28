# Surrounded Regions

## Difficulty

Medium

## Problem Description

Given a board of 'X' and 'O', capture all regions surrounded by 'X' by flipping surrounded 'O' to 'X'.

## Constraints

- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'

## Example Input/Output

Input:
[ ["X","X","X","X"],
["X","O","O","X"],
["X","X","O","X"],
["X","O","X","X"] ]
Output:
[ ["X","X","X","X"],
["X","X","X","X"],
["X","X","X","X"],
["X","O","X","X"] ]

## Step-by-Step Explanation

1. Mark all 'O' cells connected to the border as safe.
2. Flip all remaining 'O' to 'X'.
3. Restore safe cells back to 'O'.

## Optimized Approach

DFS/BFS from borders to mark safe cells.

## Time Complexity

O(m\*n)

## Space Complexity

O(m\*n)
