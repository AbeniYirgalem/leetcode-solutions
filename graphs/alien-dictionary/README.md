# Alien Dictionary

## Difficulty

Hard

## Problem Description

Given a sorted list of words from an alien language, return a possible ordering of letters. If the order is invalid, return an empty string.

## Constraints

- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of lowercase English letters

## Example Input/Output

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

## Step-by-Step Explanation

1. Compare adjacent words to infer letter ordering.
2. Build a directed graph and indegree map.
3. Topologically sort the graph.

## Optimized Approach

Topological sort with BFS (Kahn's algorithm).

## Time Complexity

O(V + E)

## Space Complexity

O(V + E)
