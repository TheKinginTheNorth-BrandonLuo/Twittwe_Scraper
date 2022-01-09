import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = 'E:/Fan_Luo_PhD/Twitter Project/data.txt'

tweets_data = []
tweets_file = open(tweets_data_path,"r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.apppend(tweet)
    except:
        continue
    tweets = pd.DataFrame()
    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
    tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
    tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

#print (len(tweets_data))
    
    
    
    

