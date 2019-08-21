#!/usr/bin/python3.6
import tweepy
from tweepy import OAuthHandler,Stream
from tweepy.streaming import StreamListener
from time import sleep


# add your tokens where the x is

CONSUMER_KEY = 'x'
CONSUMER_SECRET = 'x'
ACCESS_TOKEN = 'x'
ACCESS_TOKEN_SECRET = 'x'


# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

#create stream
myStream= tweepy.StreamListener


def get_last_id():
    """ Read the last retweeted id from a file """
    with open("lastid", "r") as fp:
        return fp.read()

def store_last_id(tweet_id):
    """ Store a tweet id in a file """
    with open("lastid","a") as fp:
        fp.write(str(tweet_id)+""+'\n')


lastid= get_last_id()

class MyStreamListener(tweepy.StreamListener):


    def on_status(self, tweet):

        str1="adivasi"

        ### this bit just means it only retweets main tweets rather than reply tweets or quote tweets

        if hasattr(tweet,'retweeted_status')==False and tweet.in_reply_to_screen_name==None and str1 in tweet.text or str1.upper() in tweet.text or str1.title() in tweet.text:
                link= "https://twitter.com/user/status/"+tweet.id_str
                tweetID= tweet.id_str

        #if statement "if the word Adivasi in the twitter post and bot hasn't already tweeted then execute nested if statement

                str2= "https://twitter.com/user/status/"

                if link not in lastid and str2 in link:

                #retweet the personthen store the tweet id
                # to make sure we aren't duplicating tweets.

                                sleep(60)
                                api.retweet(tweetID)
                                store_last_id(link)

    def on_error(self, status_code):
        if status_code == 420 or status_code==185 or status_code==327:
            #returning False in on_error disconnects the stream
            return False
        # returning non-False reconnects the stream, with backoff.

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener,wait_on_rate_limit=True)
myStream.filter(track=['adivasi'],is_async=True)
