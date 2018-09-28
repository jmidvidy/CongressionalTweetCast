# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:33:27 2018

@author: jmidv
"""

import tweepy
import json
import os



def pull(tw_ha):
    
    #might have to get rid of "@" character when linked
    twitter_handle = tw_ha
        
    CONSUMER_KEY = "Y7qbXUeaUtu4FdfgS4fBK8p8o"
    CONSUMER_SECRET = "JWwbK8QfujX00R9oVq9j65gyAQLPU4JtRxNuGcmmmsnmB7k3Wf"
    ACCESS_TOKEN = "879136248497147904-mLf2LFUDgAqfqwvVLpjJL4FzcIYgxKj"
    ACCESS_TOKEN_SECRET = "HPOsfjKTv8ctn80KvZfa1zlbxtRjgJPvdp4SbcZBzdMrv"
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    print(tw_ha)
    
    #ADD check to see if inputted user is valid 
    
    
    #get tweets
    tweets = []
    th_pull = tweepy.Cursor(api.user_timeline,screen_name=twitter_handle).items(300)
    
    #see if th_pull operated on a valid twitter user
    try:
        for t in th_pull:
            break #if iterable, then valid.  Break and move on
    except tweepy.TweepError:
        return(2) #not iterable, then invalid.  Return 2
    
    #begin iteration
    for tweet in th_pull:
        
        #see if protected
        th_user = tweet._json["user"]    
        th_privacy = th_user["protected"] 
        #if inputted user is private, return 0
        if th_privacy == True:
            return(0)
            
        if ('RT @' not in tweet.text):
            continue

        ##assemble tweets from all tweets
        t_j = tweet._json["text"]
        tweets.append(t_j)
        
    #delete all files in current json folder
    #delete all the existing models in the current directory
    curr_models = os.listdir(".\\user_tweets")
    for f in curr_models:
        fp = ".\\user_tweets\\" + f
        os.remove(fp)

    
    #write to json
    full_line = "user_tweets\\" + twitter_handle + ".json"
    json.dump(tweets, open(full_line, "w"))
        
    #return success
    return(1)
    
    
    
pull("realDonaldTrump")


