#!/usr/bin/env python3
from dotenv import load_dotenv
from mastodon import Mastodon
import os, time

#load .env and load api keys from file.
load_dotenv()
api = Mastodon(os.getenv('CLIENT_KEY'), os.getenv('CLIENT_SECRET'), os.getenv('ACCESS_TOKEN'), os.getenv('API_URL'), os.getenv('POD'))
min_id = ''

while True:
    #load local timeline
    timeline = api.timeline_local(min_id=min_id)

    #read post contents and if 'placeholder' in post favorite the post. 
    #CHANGE PLACEHOLDER
    for toot in timeline:
        if 'placeholder' in toot['content']:
            api.status_favourite(toot['id'])
            
    if len(timeline) > 0:
        min_id = timeline[0]['id']

    time.sleep(30)
