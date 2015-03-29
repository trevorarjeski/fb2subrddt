__author__ = 'Trevor Arjeski'

import ConfigParser
from GetPosts import GetPosts
from BulkPostToSubreddit import BulkPostToSubreddit

"""
This rips a Facebook group's post off of Facebook
and posts them all to a (new) subreddit.
"""

# Read config file
configParser = ConfigParser.RawConfigParser()
configParser.read('config.cfg')
facebook_cfg = dict(configParser.items('FACEBOOK'))
reddit_cfg = dict(configParser.items('REDDIT'))

# Your Facebook API access key with user_groups access
access_token = facebook_cfg['access_token']
# The id of the group you want to scrape from
group_id = facebook_cfg['group_id']

fb_getter = GetPosts(access_token, group_id)
# This will probably take a while...
fb_getter.get_all()

# reddit username
username = reddit_cfg['username']
# reddit password
password = reddit_cfg['password']
# destination subreddit
subreddit = reddit_cfg['subreddit']

r_poster = BulkPostToSubreddit(username, password, subreddit, fb_getter.get_simple_posts())
r_poster.submit_posts()

