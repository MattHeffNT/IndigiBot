#!/usr/bin/python3.64
import tweepy
from tweepy import OAuthHandler


CONSUMER_KEY = 'x'
CONSUMER_SECRET = 'x'
ACCESS_TOKEN = 'x'
ACCESS_TOKEN_SECRET = 'x'


# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


# Create API object
api = tweepy.API(auth)


#################### static twitter search  ######################

def store_last_id(tweet_id):
    """ Store a tweet id in a file """
    with open("lastid","a") as fp:
        fp.write(str(tweet_id)+'\n')


def get_last_id():
    """ Read the last retweeted id from a file """
    with open("lastid", "r") as fp:
        return fp.read()

if __name__ == '__main__':

    try:
        last_id = get_last_id()
    except FileNotFoundError:
        print("No retweet yet")
        last_id = None

    for tweet in tweepy.Cursor(api.search, q="indigenous", since_id=last_id).items(150):

         #str1 variable is literally just looking for lowercase indigenous in twitter searches, can add complexity here (i.e. lowercase aboriginal etc)
         # will also consider adding further context analysis and or machine learning capabilities   
        
        str1= "indigenous"
        str2= "https://twitter.com/user/status/"
        lastid= get_last_id()

        #if the tweet object has the retweeted_status attribute and isn't a reply to someone (can change this second condition later if we like) then store username in 
        #variable "user" and the dictionary that's in a list that's in a tuple inside the "url" variable.
        #and last condition check if the word indigenous lowercase (str1) is in the twitter post

        if hasattr(tweet,'retweeted_status') and tweet.in_reply_to_screen_name==None and str1 in (f'{tweet.text}'):
                user=tweet.retweeted_status.author.screen_name
                url=tweet.retweeted_status.entities['urls']

                # loop through url dictionary until we get the expanded url value then store this in the link variable. Then replace
                # the text with generic twitter url so that it appears as media in the bot's feed. (tweepy doesn't have quote tweet
                # functionality just yet
                
                for urls in url:
                        link=urls['expanded_url']
                        link=link.replace("https://twitter.com/i/web/status/","https://twitter.com/user/status/")

                # double check bot hasn't already tweeted the current post in memory also double check that "link" is correct url type
                        if link not in lastid and str2 in link:
                
                #tweet the person with our message then store the tweet id
                # to make sure we aren't duplicating tweets.

                                api.update_status ("@"+user+" should you be using a capital I for Indigenous? #uppercaseBlacks https://t.co/3G7C7l7y4X "+ link)
                                store_last_id(link)              

        
