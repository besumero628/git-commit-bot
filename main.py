import tweepy
import settings

# Twitter APIのキーを設定
consumer_key = settings.TWITTER_CONSUMER_API_KEY
consumer_secret = settings.TWITTER_CONSUMER_API_SECRET_KEY

# Twitter APIのアクセストークンを設定
access_token=settings.TWITTER_ACCESS_TOKEN
access_token_secret =settings.TWITTER_ACCESS_TOKEN_SECRET

# Client 作成
client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

# 投稿文の設定
client.create_tweet(text="Hello Twitter!!")