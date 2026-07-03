# Word Search II

## Difficulty

Hard

## Problem Description

Given a board of letters and a list of words, return all words that can be formed by sequentially adjacent letters.

## Constraints

- 1 <= board.length, board[0].length <= 12
- 1 <= words.length <= 3 \* 10^4
- 1 <= words[i].length <= 10

## Example Input/Output

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["oath","eat"]

## Step-by-Step Explanation

1. Build a trie of the input words.
2. DFS from each cell, following trie edges.
3. When a word ends, record it and continue.

## Optimized Approach

Trie + DFS with pruning.

## Time Complexity

O(m*n*4^L)

## Space Complexity

O(total letters in trie)
