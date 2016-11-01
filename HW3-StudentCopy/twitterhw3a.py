# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy

# Unique code from Twitter
access_token = "2208305132-4VDnZQ4iU7Jnk3a35BJnSiPvHcFO08fvGijBOzq"
access_token_secret = "6doGffK5c8QXMWkgOOmpYw5PemkgeVXsoFyyEs4ZNGGr9"
consumer_key = "lEi4ZCaCJYb0XeI1NbbT5ON7m"
consumer_secret = "sembzN32IjowIpO4MbfAuPcoCrGEBgl6Bdcs8BLMGccSW1P7RZ"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

api.update_with_media('206penguin.png', status='#UMSI-206 #Proj3')

print("success")

