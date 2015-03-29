"""
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>

Modified by Trevor Arjeski to work specifically
with facebook groups
"""
import facebook
import requests
import SimplePost


class GetPosts:
    """ Provide your access_token, a group id, and a sub directory
    that you want to search on (/feed, /events...etc)
    """

    def __init__(self, access_token, group_id):
        self.group_id = group_id
        self.group_sub = '/feed'
        self.graph = facebook.GraphAPI(access_token)
        self.simple_posts = []

    def add_simple_post(self, post):
        """ Extract author, type, message, and link from this post.
        Add it to this objects simple posts.
        """
        author = post.get('from').get('name')
        post_type = post.get('type')
        message = post.get('message')
        link = post.get('link')
        link_desc = post.get('name')
        print 'Type : %s , Author: %s, Message: %s, Description: %s, Link: %s ' % (
            post_type, author, message, link_desc, link)
        self.simple_posts.append(SimplePost.SimplePost(author, post_type, message, link, link_desc))

    def get_all(self):
        print 'Fetching posts from group.'
        search_object = self.group_id + self.group_sub
        posts = self.graph.get_object(search_object)
        print posts['data']
        # Wrap this block in a while loop so we can keep paginating requests until
        # finished.
        while True:
            try:
                # Perform some action on each post in the collection we receive from
                # Facebook.
                print 'Found %s posts ' % len(posts['data'])
                [self.add_simple_post(post=post) for post in posts['data']]
                # Attempt to make a request to the next page of data, if it exists.
                print 'Getting next page of posts...'
                posts = requests.get(posts['paging']['next']).json()
            except KeyError:
                # When there are no more pages (['paging']['next']), break from the
                # loop and end the script.
                break

    def get_simple_posts(self):
        return self.simple_posts