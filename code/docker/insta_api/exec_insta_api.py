#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "."))
from os import path
APP_ROOT = path.dirname(path.abspath(__file__))
from argparse import ArgumentParser
from insta_api import InstaApi


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--query <query>] [--help]'
    )
    arg_parser.add_argument('-q', '--query', default="", help='query')
    options = arg_parser.parse_args()

    insta_api_instance = InstaApi()

    print(insta_api_instance.search_tag(query=options.query))
