# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob
import re 
import numpy

# Unique code from Twitter
access_token = "2208305132-4VDnZQ4iU7Jnk3a35BJnSiPvHcFO08fvGijBOzq"
access_token_secret = "6doGffK5c8QXMWkgOOmpYw5PemkgeVXsoFyyEs4ZNGGr9"
consumer_key = "lEi4ZCaCJYb0XeI1NbbT5ON7m"
consumer_secret = "sembzN32IjowIpO4MbfAuPcoCrGEBgl6Bdcs8BLMGccSW1P7RZ"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('#HillaryClintonforprison')

polarity_list = []
for tweet in public_tweets:
	analysis = TextBlob(tweet.text)
	print(tweet.text)
	polarity = analysis.sentiment[0]
	polarity_list.append(polarity)
avg_polarity = numpy.mean(polarity_list)


subj_list = []
for tweet in public_tweets:
	analysis = TextBlob(tweet.text)
	print(tweet.text)
	subj = analysis.sentiment[1]
	subj_list.append(subj)
avg_subj = numpy.mean(subj_list)
print("Average subjectivity is " + str(avg_polarity))
print("Average polarity is " + str(avg_subj))