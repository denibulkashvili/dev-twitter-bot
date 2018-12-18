import tweepy
import time
import requests
import json

from dotenv import load_dotenv
load_dotenv()
import os


# Bot Settings
consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']

access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

INTERVAL = 60 * 60 * 6  # tweet every 6 hours
# INTERVAL = 15  # every 15 seconds, for testing

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_next_tweet():
    try:
        file_name = open("tweets_posted.txt", "r")
        id = file_name.read()
        next_id = int(id)+1
        file_name = open("tweets_posted.txt", "w")
        file_name.write(str(next_id))
        print(f'Next tweet id: {next_id}')
        return next_id
    except IOError:
        print("File not found or path is incorrect")
    finally:
        file_name.close()

    
    
def getQuote():
    id = get_next_tweet()
    api_quote = requests.get(f'http://quotes.stormconsultancy.co.uk/quotes/{id}.json').json()
    api_quote_author = api_quote["author"]
    api_quote_text = api_quote["quote"]
    post = f'{api_quote_text} - {api_quote_author}'
    return post
    
def tweet(post):
    api.update_status(post)
    print(f'Post tweeted:\n{post}')
    time.sleep(INTERVAL) 

while True:
    post = getQuote()
    tweet(post)
    


