# Time Based Key-Value Store

## Difficulty

Medium

## Problem Description

Design a time-based key-value store that supports set(key, value, timestamp) and get(key, timestamp) which returns the value with the largest timestamp less than or equal to the given timestamp.

## Constraints

- 1 <= key.length, value.length <= 100
- 1 <= timestamp <= 10^7
- All timestamps for a key are strictly increasing

## Example Input/Output

Input:
set("foo", "bar", 1)
get("foo", 1) -> "bar"
get("foo", 3) -> "bar"
set("foo", "bar2", 4)
get("foo", 4) -> "bar2"

## Step-by-Step Explanation

1. Store values per key in timestamp order.
2. To get a value, binary search for the rightmost timestamp <= query.

## Optimized Approach

Use a dictionary mapping keys to sorted lists of (timestamp, value). Binary search on timestamps.

## Time Complexity

set: O(1) amortized
get: O(log n)

## Space Complexity

O(n)
