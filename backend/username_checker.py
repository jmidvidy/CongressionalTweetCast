# -*- coding: utf-8 -*-
"""
Created on Fri May 25 01:40:21 2018

@author: jmidv
"""

import tweepy

CONSUMER_KEY = "Y7qbXUeaUtu4FdfgS4fBK8p8o"
CONSUMER_SECRET = "JWwbK8QfujX00R9oVq9j65gyAQLPU4JtRxNuGcmmmsnmB7k3Wf"
ACCESS_TOKEN = "879136248497147904-mLf2LFUDgAqfqwvVLpjJL4FzcIYgxKj"
ACCESS_TOKEN_SECRET = "HPOsfjKTv8ctn80KvZfa1zlbxtRjgJPvdp4SbcZBzdMrv"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

twitter_handle = "wedwedwewfrerferferfevwevwer"


def main():

    th_pull = tweepy.Cursor(api.user_timeline,screen_name=twitter_handle).items(300)
    
    try:
        for tweet in th_pull:
            break
    except:
        print("error")
        return
    
    print("got here")

        
main() 

        
    

