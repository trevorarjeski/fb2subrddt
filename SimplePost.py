__author__ = 'Trevor Arjeski'


class SimplePost:

    def __init__(self, author, post_type, message, link, link_desc):
        self.author = author
        self.post_type = post_type
        self.message = message
        self.link = link
        self.link_desc = link_desc
        self.check_link()

    def get_short_message(self):
        return ' '.join(self.message.split()[:3])

    def check_link(self):
        if self.link is not None:
            self.message = None

    def get_title(self):
        if self.link is not None:
            return self.link_desc
        if self.message is not None:
            return self.message
        else:
            return self.author + ': no title'

    def get_type(self):
        return self.post_type

    def get_message(self):
        return self.message

    def get_link(self):
        return self.link

    def get_link_description(self):
        return self.link_desc
