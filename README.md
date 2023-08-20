# favbot
A mastodon bot that searches the local timeline for posts containing specified text and favorite those posts.

# Dependencies 

* python3
* pip
* mastodon.py

```
pip install mastodon.py
```

# Configuration

To configure bot open dotfile .env and enter keys from mastodon application which you can create in Settings > Development > New Application
Bot needs permissions to write favorites so remember to specify when creating application in mastodon settings.

```
CLIENT_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
CLIENT_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ACCESS_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
API_URL=https://(yourdomain)/api/V1/
```

Once .env is configured you must open main.py and edit 'placeholder' on line 18 to change text search parameters in the content of post
(If you'd like the bot to favorite all posts on the local timeline you can simply delete the if statement):

```
if 'placeholder' in toot['content']:
```

Application can be started using

```
python3 main.py
```
