# Asteroid Collision

## Difficulty

Medium

## Problem Description

Given a list of asteroids represented by integers, positive values move right and negative values move left. When two asteroids collide, the smaller one explodes; if equal, both explode. Return the state after all collisions.

## Constraints

- 1 <= asteroids.length <= 10^4
- -1000 <= asteroids[i] <= 1000
- asteroids[i] != 0

## Example Input/Output

Input: asteroids = [5, 10, -5]
Output: [5, 10]

## Step-by-Step Explanation

1. Use a stack to store asteroids moving to the right.
2. When a left-moving asteroid appears, it may collide with right-moving ones in the stack.
3. Resolve collisions until the asteroid is destroyed or no collision remains.

## Optimized Approach

Simulate collisions with a stack, only resolving when directions conflict.

## Time Complexity

O(n)

## Space Complexity

O(n)
