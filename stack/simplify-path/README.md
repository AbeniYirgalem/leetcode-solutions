# Simplify Path

## Difficulty

Medium

## Problem Description

Given a Unix-style file path, simplify it and return the canonical path.

## Constraints

- 1 <= path.length <= 3000
- path consists of letters, digits, '.', '/', and '\_'

## Example Input/Output

Input: path = "/a/./b/../../c/"
Output: "/c"

## Step-by-Step Explanation

1. Split the path by '/'.
2. Use a stack to process directories.
3. Handle '.', '..', and empty parts accordingly.

## Optimized Approach

Stack-based normalization.

## Time Complexity

O(n)

## Space Complexity

O(n)
