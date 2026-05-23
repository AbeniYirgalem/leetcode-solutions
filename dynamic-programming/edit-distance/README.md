# Edit Distance

## Difficulty

Hard

## Problem Description

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2. Operations: insert, delete, replace.

## Constraints

- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters

## Example Input/Output

Input: word1 = "horse", word2 = "ros"
Output: 3

## Step-by-Step Explanation

1. dp[i][j] is the min operations to convert word1[0:i] to word2[0:j].
2. If characters match, copy dp[i-1][j-1].
3. Otherwise, take min of insert, delete, replace.

## Optimized Approach

Classic 2D dynamic programming.

## Time Complexity

O(m\*n)

## Space Complexity

O(m\*n)
