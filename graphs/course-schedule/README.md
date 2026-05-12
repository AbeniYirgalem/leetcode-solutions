# Course Schedule

**Difficulty:** Medium

## Problem Description

You are given a number of courses and prerequisite pairs. Return true if it is possible to finish all courses (i.e., the prerequisite graph has no cycle).

## Examples

**Input:** numCourses = 2, prerequisites = [[1,0]]
**Output:** true

**Input:** numCourses = 2, prerequisites = [[1,0],[0,1]]
**Output:** false

## Step-by-Step Approach

1. Build a directed graph and compute in-degrees.
2. Use Kahn's algorithm (BFS) to remove nodes with zero in-degree.
3. If all courses are processed, the graph is acyclic.

## Time and Space Complexity

- **Time:** O(V + E)
- **Space:** O(V + E)
