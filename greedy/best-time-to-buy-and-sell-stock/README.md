# Best Time to Buy and Sell Stock

**Difficulty:** Easy

## Problem Description

Given an array where each element is a stock price on a given day, find the maximum profit from one buy and one sell. If no profit is possible, return 0.

## Examples

**Input:** prices = [7,1,5,3,6,4]
**Output:** 5

**Input:** prices = [7,6,4,3,1]
**Output:** 0

## Step-by-Step Approach

1. Track the minimum price seen so far.
2. For each price, compute the profit if sold today.
3. Update the maximum profit whenever a higher value is found.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(1)
