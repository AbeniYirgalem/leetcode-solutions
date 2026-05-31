# Top K Frequent Words

## Difficulty

Medium

## Problem Description

Given a list of words, return the k most frequent words. Sort by frequency descending, then lexicographically.

## Constraints

- 1 <= words.length <= 500
- 1 <= k <= number of unique words

## Example Input/Output

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]

## Step-by-Step Explanation

1. Count word frequencies.
2. Sort by (-freq, word).
3. Take the first k words.

## Optimized Approach

Sort by custom key.

## Time Complexity

O(n log n)

## Space Complexity

O(n)
