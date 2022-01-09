#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from urllib3.exceptions import ProtocolError
from requests.exceptions import ChunkedEncodingError
from http.client import IncompleteRead


#Variables that contains the user credentials to access Twitter API 
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            print (data)
            savefile = open("f://py programs/Twitter Project/fifa worldcup.txt","a")
            savefile.write(data)
            savefile.write('\n')
            savefile.close()
            return True
        except BaseException.e:
            print ("Failed on Data", str(e))
            time.sleep(5)
    

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    while True:
           
        try:
            stream.filter(track = ['Fifa Worldcup'], async = True)

        except(ProtocolError, AttributeError):
            continue
        

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['childhood obesity','football worldcup','cancer','bitcoin'])

