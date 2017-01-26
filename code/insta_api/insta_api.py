#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
import yaml
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "."))
from os import path
APP_ROOT = path.dirname(path.abspath(__file__))
from instagram.client import InstagramAPI

recent_media, next_ = api.user_recent_media(user_id="userid", count=10)
for media in recent_media:
   print media.caption.text

class InstaApi(object):
    """
    Instagram api search
    """

    def __init__(self):
        config_file = APP_ROOT + "/conf/api_setting.yml"
        with open(config_file, encoding="utf-8") as cf:
            e = yaml.load(cf)
            client_id = e["client_id"]
            access_token = e["access_token"]
            client_secret = e["secret"]
        self.api = InstagramAPI(access_token=access_token, client_secret=client_secret)

    def search_tag(self, query):
        self.api.tag_search(query, count)
