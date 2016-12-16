# -*- coding: utf-8 -*-

"""fb_parser.py
HTMLParser subclass for scraping facebook html data
"""

import csv
from HTMLParser import HTMLParser 

STATE_START = -1
STATE_CHECK_USERNAME = 0
STATE_IS_CHIRAG = 1
STATE_GRAB_MSG = 2

class FBParser(HTMLParser):
    def __init__(self, writer):
        # initialize the base class
        HTMLParser.__init__(self)
        self.state = STATE_START
        self.writer = writer

    def handle_starttag(self, tag, attrs):
        if ('class', 'user') in attrs:
            self.state = STATE_CHECK_USERNAME
        elif self.state == STATE_IS_CHIRAG and tag == 'p':
            self.state = STATE_GRAB_MSG

    def handle_data(self, data):
        if self.state == STATE_CHECK_USERNAME:
            if data == 'Chirag Davé':
                self.state = STATE_IS_CHIRAG
            else:
                self.state = STATE_START
        elif self.state == STATE_GRAB_MSG:
            self.writer.writerow({'source': 'fb', 'content': data})
            self.state = STATE_START

