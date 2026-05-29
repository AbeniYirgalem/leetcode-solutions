# Design Twitter

## Difficulty

Medium

## Problem Description

Design a simplified Twitter that supports posting tweets, following/unfollowing users, and retrieving the 10 most recent tweets in the news feed.

## Constraints

- 1 <= userId, tweetId <= 10^4
- Each user can follow/unfollow any user, including themselves

## Example Input/Output

Input:
postTweet(1, 5)
getNewsFeed(1) -> [5]
follow(1, 2)
postTweet(2, 6)
getNewsFeed(1) -> [6, 5]

## Step-by-Step Explanation

1. Store each user's tweets with a timestamp.
2. Track follow relationships.
3. Merge recent tweets from the user and followees using a heap.

## Optimized Approach

Use a max-heap over the latest tweet of each followed user for efficient merging.

## Time Complexity

postTweet: O(1)
getNewsFeed: O(10 log f) where f is number of followed users

## Space Complexity

O(t)
