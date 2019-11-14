import tweepy
from tweepy import OAuthHandler,Stream
from tweepy.streaming import StreamListener
from time import sleep

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

        str1="indigenous"
        str3="torres straight"
        notweet= ""
        acceptable= ""

        collocations= ({" plants"," animals"," reptiles" " species"," herbs"," fruits"," birds"," mammals"," fish",
                             " to", " to "," variety"," flora"," fauna"," British"," Brits","brit","Brit"})

        context_dictionary= ({"chandrayaan","Chandrayaan","ISRO","miners kill", "Brazil murder", "indigenously", 
                        "indigenous to","indigenous red grape","indigenous grape","Amazon gold miners","indigenous/native plants",
                        "indigenous cows","Brazil miners"})

        
        # loop  to add the word indigenous with collocations to check in the conditional later
        for i in collocations:
                acceptable= str1+i
        

        # loop and check for common words and contexts to ignore
        for word in context_dictionary:
            if word in tweet.text:
                    noTweet= word
        else:
                noTweet=""


                #we don't want to capture retweeted tweets for live streamed, 
                #this condition also checks for strings in dictionaries above.

        if (hasattr(tweet,'retweeted_status')==False and tweet.in_reply_to_screen_name==None and 
            str1 in tweet.text and acceptable not in tweet.text and noTweet ==""):
            
                #create Twitter link using the ID string attribute (to later save to database).
                #getting the TweetID attribute will allow the bot to retweet the tweet.
 
                link= "https://twitter.com/user/status/"+tweet.id_str
                tweetID= tweet.id_str
                user= tweet.user.screen_name


  

                str2= "https://twitter.com/user/status/"
    
          #if the word indigenous in the twitter post and bot hasn't already tweeted that tweet 
          #then sleep (to avoid Twitter ban) , retweet the tweet, then store the link to database.

                if link not in lastid and str2 in link:

                #retweet then store the tweet id
                # to make sure we aren't duplicating tweets.

                                sleep(60)
                                api.retweet(tweetID)
                                store_last_id(link)


        # if the tweet has torres straight then retweet them

        elif (hasattr(tweet,'retweeted_status')==False and tweet.in_reply_to_screen_name==None and 
              str3.title() in tweet.text or str3 in tweet.text or str3.upper() in tweet.text or str3.capitalize() in tweet.text):
            
                link= "https://twitter.com/user/status/"+tweet.id_str
                tweetID= tweet.id_str
                str2= "https://twitter.com/user/status/"

                if link not in lastid and str2 in link:
                                sleep(60)
                                api.retweet(tweetID)
                                store_last_id(link)


    def on_error(self, status_code):
        if status_code == 420 or status_code==185 or status_code==327:
            #returning False in on_error disconnects the stream
            return False
        # returning non-False reconnects the stream, with backoff.

#start Tweepy functions/class methods
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener,wait_on_rate_limit=True)
myStream.filter(track=['indigenous,torres straight'],is_async=True)
