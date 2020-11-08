#!/usr/bin/env python3
import praw
import os


client_id     = os.getenv('REDDIT_ID') 
client_secret = os.getenv('REDDIT_SECRET') 
client_password = os.getenv('REDDIT_PASSWORD') 
client_user = os.getenv('REDDIT_USER') 

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=client_password,
                     user_agent=f"testscript by u/{client_user}",
                     username=client_user)

print(reddit.user.me())
