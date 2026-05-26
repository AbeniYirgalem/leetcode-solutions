# Open the Lock

## Difficulty

Medium

## Problem Description

You have a lock with 4 wheels. Given deadends and a target, return the minimum number of turns to open the lock, or -1 if impossible.

## Constraints

- 1 <= deadends.length <= 500
- target is a 4-digit string

## Example Input/Output

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6

## Step-by-Step Explanation

1. Use BFS from "0000".
2. At each state, generate 8 neighbors by turning one wheel.
3. Stop when the target is reached.

## Optimized Approach

Standard BFS with a visited set.

## Time Complexity

O(10^4)

## Space Complexity

O(10^4)
