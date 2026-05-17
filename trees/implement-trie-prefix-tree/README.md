# Implement Trie (Prefix Tree)

**Difficulty:** Medium

## Problem Description

Implement a trie with insert, search, and startsWith operations.

## Examples

**Input:** insert("apple"), search("apple"), search("app"), startsWith("app")
**Output:** true, false, true

**Input:** insert("app"), search("app")
**Output:** true

## Step-by-Step Approach

1. Each node keeps a map of child characters and an end-of-word flag.
2. Insert walks or creates nodes for each character.
3. Search and prefix checks walk nodes and validate end-of-word when needed.

## Time and Space Complexity

- **Time:** O(L) per operation
- **Space:** O(total characters)
