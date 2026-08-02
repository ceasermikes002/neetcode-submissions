from collections import defaultdict
from heapq import heappush, nlargest

class Twitter:
    def __init__(self):
        self.users = defaultdict(set)  # Maintain follow relationships as directed graph
        self.tweets = defaultdict(list)  # Each user's list of tweets, with timestamps
        self.timestamp = 0  # Simulate global timestamp to order the tweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append the tweet with timestamp
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list:
        # Use a min-heap to efficiently retrieve the 10 most recent tweets
        min_heap = []
        # Add user's own tweets and those they follow
        for user in self.users[userId] | {userId}:
            for tweet in self.tweets[user]:
                heappush(min_heap, tweet)
                if len(min_heap) > 10:
                    min_heap = nlargest(10, min_heap)  # Keep only the top 10 recent tweets in the heap
        min_heap.sort(reverse=True)  # Order tweets in descending order before getting ids
        return [tweetId for _, tweetId in min_heap]

    def follow(self, followerId: int, followeeId: int) -> None:
        # Ensure no self-follow but add a follow relationship
        if followerId != followeeId:
            self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Safely remove a follow relationship if it exists
        self.users[followerId].discard(followeeId)