# Encode and Decode Strings

**Difficulty:** Medium

## Problem Description

Design an algorithm to encode a list of strings to a single string and decode it back.

## Examples

**Input:** ["lint","code","love","you"]
**Encoded:** "4#lint4#code4#love3#you"
**Decoded:** ["lint","code","love","you"]

**Input:** [""]
**Encoded:** "0#"
**Decoded:** [""]

## Step-by-Step Approach

1. Encode each string as: length + '#' + string.
2. While decoding, parse the length, then read that many characters.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(n)
