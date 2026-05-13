# Word Ladder

**Difficulty:** Hard

## Problem Description

Given a start word, an end word, and a dictionary, find the shortest number of transformations from start to end. Each step can change exactly one letter and the new word must be in the dictionary.

## Examples

**Input:** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
**Output:** 5

**Input:** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
**Output:** 0

## Step-by-Step Approach

1. Build an intermediate pattern map (e.g., h\*t -> hot, hit).
2. Use BFS from the begin word to find the shortest path.
3. Each layer in BFS represents one transformation step.

## Time and Space Complexity

- **Time:** O(N \* L^2) where N is number of words and L is word length
- **Space:** O(N \* L)
