#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "."))
from os import path
APP_ROOT = path.dirname(path.abspath(__file__))
from argparse import ArgumentParser
from line_api import *


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)