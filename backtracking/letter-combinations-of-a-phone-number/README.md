# Letter Combinations of a Phone Number

## Difficulty

Medium

## Problem Description

Given a string of digits from 2-9, return all possible letter combinations that the number could represent on a phone keypad. Return an empty list if the input is empty.

## Constraints

- 0 <= digits.length <= 4
- digits[i] is in the range '2' to '9'

## Example Input/Output

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

## Step-by-Step Explanation

1. Map each digit to its possible letters.
2. Use backtracking to build combinations character by character.
3. When the current string reaches the input length, add it to results.

## Optimized Approach

Backtracking generates only valid combinations and avoids extra processing.

## Time Complexity

O(3^n \* n) to build each string (worst case 4^n for digit 7/9)

## Space Complexity

O(n) recursion depth, excluding output
