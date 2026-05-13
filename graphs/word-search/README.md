# Word Search

**Difficulty:** Medium

## Problem Description

Given an m x n board of letters and a word, return true if the word exists in the grid. The word must be constructed from sequentially adjacent cells (horizontally or vertically), and each cell may be used at most once.

## Examples

**Input:** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
**Output:** true

**Input:** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
**Output:** true

## Step-by-Step Approach

1. Try each cell as a start position.
2. Use DFS with backtracking to match characters in order.
3. Mark a cell as visited during the path, then unmark on backtrack.

## Time and Space Complexity

- **Time:** O(m _ n _ 4^L) where L is word length
- **Space:** O(L)
