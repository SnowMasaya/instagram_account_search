#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
from flask import Flask, request, abort
import yaml
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "."))
from os import path
APP_ROOT = path.dirname(path.abspath(__file__))

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


app = Flask(__name__)

config_file = APP_ROOT + "/conf/api_setting.yml"
with open(config_file, encoding="utf-8") as cf:
    e = yaml.load(cf)
    line_bot_api = LineBotApi(e["access_token"])
    handler = WebhookHandler(e["secret"])

@app.route("/callback", methods=['POST'])
def callback(self):
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(self, event, message):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message))
