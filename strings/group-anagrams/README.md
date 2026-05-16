# Group Anagrams

**Difficulty:** Medium

## Problem Description

Given an array of strings, group the anagrams together and return the groups in any order.

## Examples

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]
**Output:** [["eat","tea","ate"],["tan","nat"],["bat"]]

**Input:** strs = [""]
**Output:** [[""]]

## Step-by-Step Approach

1. Use a hash map from sorted string to list of anagrams.
2. For each string, sort it to get the key and append it to the group.

## Time and Space Complexity

- **Time:** O(n \* k log k) where k is average word length
- **Space:** O(n \* k)
