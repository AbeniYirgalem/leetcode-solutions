# Accounts Merge

## Difficulty

Medium

## Problem Description

Given a list of accounts where each account has a name and emails, merge accounts that share any email.

## Constraints

- 1 <= accounts.length <= 1000
- 2 <= accounts[i].length <= 10
- 1 <= accounts[i][j].length <= 30

## Example Input/Output

Input: accounts = [["John","johnsmith@mail.com","john00@mail.com"],["John","johnnybravo@mail.com"],["John","johnsmith@mail.com","john_newyork@mail.com"],["Mary","mary@mail.com"]]
Output: merged accounts with sorted emails

## Step-by-Step Explanation

1. Union emails that appear in the same account.
2. Group emails by their root parent.
3. Build output by sorting emails and attaching the name.

## Optimized Approach

Union-Find on emails with hashing.

## Time Complexity

O(n _ a _ alpha(n))

## Space Complexity

O(n \* a)
