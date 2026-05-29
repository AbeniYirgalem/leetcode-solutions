from typing import List, Dict, Set, Tuple
import heapq


class Twitter:
    def __init__(self) -> None:
        self.time = 0
        self.tweets: Dict[int, List[Tuple[int, int]]] = {}
        self.following: Dict[int, Set[int]] = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets.setdefault(userId, []).append((self.time, tweetId))
        self.following.setdefault(userId, set()).add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following:
            return []
        heap: List[Tuple[int, int, int]] = []
        for uid in self.following[userId]:
            if uid in self.tweets and self.tweets[uid]:
                time, tid = self.tweets[uid][-1]
                heapq.heappush(heap, (-time, uid, len(self.tweets[uid]) - 1))
        result: List[int] = []
        while heap and len(result) < 10:
            neg_time, uid, idx = heapq.heappop(heap)
            result.append(self.tweets[uid][idx][1])
            if idx > 0:
                time, _ = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (-time, uid, idx - 1))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set()).add(followeeId)
        self.following[followerId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId != followerId:
            self.following[followerId].discard(followeeId)


if __name__ == "__main__":
    tw = Twitter()
    tw.postTweet(1, 5)
    print(tw.getNewsFeed(1))
    tw.follow(1, 2)
    tw.postTweet(2, 6)
    print(tw.getNewsFeed(1))
    tw.unfollow(1, 2)
    print(tw.getNewsFeed(1))
