import tweepy
import time
import requests
import json

from dotenv import load_dotenv
load_dotenv()
import os


consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']

access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']


INTERVAL = 60 * 60 * 6  # tweet every 6 hours
# INTERVAL = 15  # every 15 seconds, for testing

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


while True:
    api_quote = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    api_quote_id = api_quote["id"]
    api_quote_author = api_quote["author"]
    api_quote_text = api_quote["quote"]
    post = f'{api_quote_text} - {api_quote_author}'
    
    api.update_status(post)
    print(f'Post tweeted:\n{post}')
    time.sleep(INTERVAL) 


