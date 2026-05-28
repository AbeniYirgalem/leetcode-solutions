# Gas Station

## Difficulty

Medium

## Problem Description

Given two arrays gas and cost, return the starting gas station index if you can travel around the circuit once, otherwise return -1.

## Constraints

- 1 <= gas.length <= 10^5
- gas.length == cost.length
- 0 <= gas[i], cost[i] <= 10^4

## Example Input/Output

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3

## Step-by-Step Explanation

1. If total gas is less than total cost, return -1.
2. Track a running tank and candidate start index.
3. Reset start when the tank drops below zero.

## Optimized Approach

Single pass greedy scan with total feasibility check.

## Time Complexity

O(n)

## Space Complexity

O(1)
