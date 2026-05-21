# Letter Tile Possibilities

## Difficulty

Medium

## Problem Description

Given tiles with letters, return the number of possible non-empty sequences.

## Constraints

- 1 <= tiles.length <= 7
- tiles consist of uppercase English letters

## Example Input/Output

Input: tiles = "AAB"
Output: 8

## Step-by-Step Explanation

1. Count frequency of each letter.
2. Try placing each available letter and recurse.
3. Count each valid sequence formed.

## Optimized Approach

Backtracking using counts to avoid duplicates.

## Time Complexity

O(n \* n!)

## Space Complexity

O(n)
