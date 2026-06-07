# Decode String

## Difficulty

Medium

## Problem Description

Given an encoded string, decode it. The encoding rule is k[encoded_string], repeated k times.

## Constraints

- 1 <= s.length <= 30
- s consists of digits, letters, and brackets

## Example Input/Output

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

## Step-by-Step Explanation

1. Use stacks to store previous strings and repeat counts.
2. When ']' appears, pop and build the repeated block.
3. Append to the previous string context.

## Optimized Approach

Stack-based parsing.

## Time Complexity

O(n)

## Space Complexity

O(n)
