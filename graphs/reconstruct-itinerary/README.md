# Reconstruct Itinerary

## Difficulty

Hard

## Problem Description

Given flight tickets [from, to], reconstruct the itinerary starting from "JFK". If multiple valid itineraries exist, return the lexicographically smallest.

## Constraints

- 1 <= tickets.length <= 300
- tickets[i].length == 2

## Example Input/Output

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

## Step-by-Step Explanation

1. Build adjacency lists with destinations in min-heap order.
2. Perform Hierholzer's algorithm to build the Eulerian path.
3. Reverse the result at the end.

## Optimized Approach

DFS with min-heap for lexicographic order.

## Time Complexity

O(E log E)

## Space Complexity

O(E)
