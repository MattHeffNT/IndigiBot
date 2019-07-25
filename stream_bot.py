import tweepy
from tweepy import OAuthHandler,Stream
from notify_run import Notify
from tweepy.streaming import StreamListener

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

str1="indigenous"
lastid= get_last_id()

class MyStreamListener(tweepy.StreamListener):

    
    def on_status(self, tweet):

        context_dictionary={" plants"," animals"," species"," herbs"," fruits"," birds"," mammals"," fish"," to"," space technology"," space programme"}

        for i in context_dictionary:

                acceptable= str1+i

                #if the tweet object has the retweeted_status attribute and isn't a reply to someone (can change this second condition later if we like) then store username in
                # variable "user" and the dictionary that's in a list that's in a tuple inside the "url" variable.

                if acceptable in tweet.text  or "chandrayaan" in tweet.text or "Chandrayaan" in tweet.text or "ISRO" in tweet.text:

                        break


                elif hasattr(tweet,'retweeted_status') and tweet.in_reply_to_screen_name==None and str1 in (f'{tweet.text}'):
                        user=tweet.retweeted_status.author.screen_name
                        url=tweet.retweeted_status.entities['urls']

                        # loop through url dictionary until we get the expanded url value then store this in the link variable.

                        for urls in url:
                                global link
                                link = urls['expanded_url']
                                link=link.replace("https://twitter.com/i/web/status/","https://twitter.com/user/status/")

                        str2= "https://twitter.com/user/status/"


                        if link not in lastid and str2 in link:

                #tweet the person with our message then store the tweet id
                # to make sure we aren't duplicating tweets.

                                #api.update_status ("@"+user+" should you be using a capital I for Indigenous? #uppercaseBlacks https://t.co/3G7C7l7y4X  "+ link)
                                print ("@"+user+" should you be using a capital I for Indigenous? #uppercaseBlacks https://t.co/3G7C7l7y4X  "+ link)
                                print ("with RT status")
                                store_last_id(link)
                                break

                        else:

                                continue

                #new parameter to capture more tweets..same as above except for not RT tweets

                elif hasattr(tweet,'retweeted_status')==False and tweet.in_reply_to_screen_name==None and str1 in (f'{tweet.text}'):
                        link= "https://twitter.com/user/status/"+tweet.id_str
                        user= tweet.user.screen_name


        #if statement "if the word indigenous in the twitter post and bot hasn't already tweeted then execute nested if statement

                        str2= "https://twitter.com/user/status/"

                        if link not in lastid and str2 in link:

                #tweet the person with our message then store the tweet id
                # to make sure we aren't duplicating tweets.

                                #api.update_status ("@"+user+" should you be using a capital I for Indigenous? #uppercaseBlacks https://t.co/3G7C7l7y4X  "+ link)
                                print ("@"+user+" should you be using a capital I for Indigenous? #uppercaseBlacks https://t.co/3G7C7l7y4X  "+ link)
                                print ("without RT status")
                                store_last_id(link)
                                break


                        else:
                                continue


    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False
        # returning non-False reconnects the stream, with backoff.
    

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=[str1],is_async=True)



