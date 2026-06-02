# LRU Cache

## Difficulty

Medium

## Problem Description

Design a least recently used (LRU) cache with get and put operations in O(1) time.

## Constraints

- 1 <= capacity <= 3000
- 0 <= key, value <= 10^4
- At most 2 \* 10^5 operations

## Example Input/Output

Input:
LRUCache(2)
put(1,1)
put(2,2)
get(1) -> 1
put(3,3)
get(2) -> -1

## Step-by-Step Explanation

1. Use a hash map for O(1) access to nodes.
2. Use a doubly linked list to track usage order.
3. Move accessed nodes to the front and evict from the back.

## Optimized Approach

Combine a hashmap with a doubly linked list for O(1) operations.

## Time Complexity

O(1) per operation

## Space Complexity

O(capacity)
