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


        for i in context_dictionary:
                acceptable= str1+i

                #if the tweet object has the retweeted_status attribute and isn't a reply to someone 
                #(can change this second condition later if we like) then store username in
                # variable "user" and the dictionary that's in a list that's in a tuple inside the "url" variable.

        for word in collocations:
            if word in tweet.text:
                    noTweet= word
        else:
                noTweet=""


                #we don't want to capture retweeted tweets for live streamed, 
                #this condition also checks for strings in dictionaries above.

        if (hasattr(tweet,'retweeted_status')==False and tweet.in_reply_to_screen_name==None and 
            str1 in tweet.text and acceptable not in tweet.text and noTweet ==""):

                link= "https://twitter.com/user/status/"+tweet.id_str
                tweetID= tweet.id_str
                user= tweet.user.screen_name


        #if statement "if the word indigenous in the twitter post and bot hasn't already tweeted then execute nested if statement

                str2= "https://twitter.com/user/status/"

                if link not in lastid and str2 in link:

                #tweet the person with our message then store the tweet id
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

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener,wait_on_rate_limit=True)
myStream.filter(track=['indigenous,torres straight'],is_async=True)
