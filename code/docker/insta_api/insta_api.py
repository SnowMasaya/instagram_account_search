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


class InstaApi(object):
    """
    Instagram api search
    Reference:
        http://stackoverflow.com/questions/16496511/how-to-get-an-instagram-access-token
        https://bobmckay.com/web/simple-tutorial-for-getting-an-instagram-clientid-and-access-token/
        About the access token
        http://www.harimanics.co.jp/blog/detail/?id=BG0057
    """

    def __init__(self):
        config_file = APP_ROOT + "/conf/api_setting.yml"
        with open(config_file, encoding="utf-8") as cf:
            e = yaml.load(cf)
            client_id = e["client_id"]
            access_token = e["access_token"]
            client_secret = e["secret"]
        try:
            self.api = InstagramAPI(access_token=access_token, client_secret=client_secret)
        except Exception as e:
            print(e)

    def search_tag(self, query):
        content = "<h2>Tag Search</h2>"
        tag_search, next_tag = self.api.tag_search(q="backclimateaction")
        tag_recent_media, next = self.api.tag_recent_media(tag_name=query)
        photos = []
        for tag_media in tag_recent_media:
            photos.append('<img src="%s"/>' % tag_media.get_standard_resolution_url())
        content += ''.join(photos)
        return "%s %s <br/>Remaining API Calls = %s/%s" % (get_nav(), content, api.x_ratelimit_remaining,
                                                           api.x_ratelimit)

