# Partition Labels

## Difficulty

Medium

## Problem Description

Given a string, partition it into as many parts as possible so that each letter appears in at most one part. Return the sizes of the parts.

## Constraints

- 1 <= s.length <= 500
- s consists of lowercase English letters

## Example Input/Output

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]

## Step-by-Step Explanation

1. Record the last index for each character.
2. Expand the current partition to the farthest last index seen.
3. When you reach that index, close the partition.

## Optimized Approach

Single pass with last-occurrence tracking.

## Time Complexity

O(n)

## Space Complexity

O(1)
