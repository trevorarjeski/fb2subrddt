__author__ = 'Trevor Arjeski'

import praw
from SimplePost import SimplePost


class BulkPostToSubreddit:
    def __init__(self, username, password, subreddit, posts):
        self.username = username
        self.password = password
        self.subreddit = subreddit
        self.posts = posts
        self.r = praw.Reddit(user_agent='Convert Facebook Group To Subreddit')
        self.r.login(username, password)

    def submit_posts(self):
        print 'Bulk posting'
        i = 0
        total = len(self.posts)
        for post in self.posts:
            i += 1
            print '%s/%s' % (i, total)
            try:
                self.submit_post(post)
            except:
                continue

    def submit_post(self, post):
        if isinstance(post, SimplePost):
            self.r.submit(self.subreddit,
                          post.get_title(),
                          post.get_message(),
                          post.get_link())