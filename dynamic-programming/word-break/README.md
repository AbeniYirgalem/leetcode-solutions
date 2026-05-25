# Word Break

## Difficulty

Medium

## Problem Description

Given a string s and a dictionary of words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

## Constraints

- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20

## Example Input/Output

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true

## Step-by-Step Explanation

1. Use dp[i] to indicate if s[0:i] can be segmented.
2. For each i, check words ending at i.
3. If dp[j] is true and s[j:i] is a word, mark dp[i] true.

## Optimized Approach

Use a set for fast lookup and limit checks by the max word length.

## Time Complexity

O(n \* m) where m is max word length

## Space Complexity

O(n)
