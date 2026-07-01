# Design Add and Search Words Data Structure

## Difficulty

Medium

## Problem Description

Implement a data structure that supports adding words and searching with '.' wildcard that matches any letter.

## Constraints

- 1 <= word.length <= 25
- word consists of lowercase English letters
- At most 10^4 operations

## Example Input/Output

Input:
addWord("bad")
addWord("dad")
search(".ad") -> true
search("b..") -> true

## Step-by-Step Explanation

1. Use a trie to store words.
2. For search, DFS through the trie when '.' appears.

## Optimized Approach

Trie with DFS for wildcard searches.

## Time Complexity

addWord: O(L)
search: O(L \* 26) in worst case

## Space Complexity

O(total letters)
