import creds
import tweepy
import aitest
client = tweepy.Client(creds.bearer_token, creds.api_key, creds.api_key_secret, creds.access_token, creds.access_token_secret)
client.create_tweet(text=aitest.justText)
print("I am the file that creates that does the tweeting itself")