import tweepy
from configparser import SafeConfigParser
import csv
import pandas as pd

parser = SafeConfigParser()
parser.read('./lib/twitter.ini')

consumer_key = parser.get('twitter', 'consumer_key')
consumer_secret = parser.get('twitter', 'consumer_secret')
access_token = parser.get('twitter', 'access_token')
access_token_secret = parser.get('twitter', 'access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

output_csv = open('csta.csv', 'a')

writer = csv.writer(output_csv)

for tweet in tweepy.Cursor(api.search, q="#csta2018").items():
    print(tweet.text)
    writer.writerow([tweet.created_at, tweet.text.encode('utf-8')])
