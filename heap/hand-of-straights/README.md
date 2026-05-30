# Hand of Straights

## Difficulty

Medium

## Problem Description

Given an array hand and an integer groupSize, return true if the hand can be rearranged into groups of groupSize consecutive cards.

## Constraints

- 1 <= hand.length <= 10^4
- 1 <= hand[i] <= 10^9
- 1 <= groupSize <= hand.length

## Example Input/Output

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true

## Step-by-Step Explanation

1. Count each card value.
2. Always start from the smallest available card.
3. Try to build a consecutive group of length groupSize.

## Optimized Approach

Use a min-heap for the smallest card and a counter for counts.

## Time Complexity

O(n log n)

## Space Complexity

O(n)
