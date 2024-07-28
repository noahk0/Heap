class Twitter:

    def __init__(self):
        self.tweets, self.following = [], defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.following[userId].add(userId)

        return [tweet[1] for tweet in self.tweets[::-1] if tweet[0] in self.following[userId]][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
