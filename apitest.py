import creds
import tweepy

print('hello')

client = tweepy.Client(creds.bearer_token, creds.api_key, creds.api_key_secret, creds.access_token, creds.access_token_secret)

client.create_tweet(text='still works lol')
print('made a tweet')