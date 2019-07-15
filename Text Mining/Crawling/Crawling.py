from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# variable that contains the user credentials to access Twitter API
access_token = "1558940846-zetaPhMq3cDzkK8xdXvod9S45ERxeVwKZpkf88s"
access_token_secret = "lxuvDHcfAMhafVuOPVsF1m33b0rCeSWfVBGHEgzwzRVSe"
consumer_key = "3ncfCFtuHiQzZRvIgIH6YYNTU"
consumer_secret = "VboOTxKdmsscZ6gIL8hOXfeHbcsW8Qg21YIIRyD5eCeDgCitDc"

# this is the basic listener that just prints received tweets to stdout
class StdOutListener(StreamListener):
    def on_data(self, data):
        #print ("%s\n" % data)
        #return True
        with open("DTCRW.txt", "a") as tweet_log:
            tweet_log.write(data)
            
    def on_error(self, status):
        print (status)


l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)


stream.filter(locations=[106.20, -6.41, 107.19, -6.01])