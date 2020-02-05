#!/usr/bin/env python3

import sys
import os
import time
from threading import Thread

from gevent import pywsgi
import requests

import settings
from chatserver import Chat

try:
    os.mkdir(settings.DATA_DIR)
except FileExistsError:
    pass


def get_chat():
    return requests.get(f'http://127.0.0.1:{CHAT_SERVER_PORT}/getchat/0').text

def show_chat_forever():
    while True:
        print(time.time(), get_chat())
        time.sleep(1)

CHAT_SERVER_PORT = 5000
USER = "guest"

try:
    if sys.argv[1] == 'daemon':
        try:
            server = pywsgi.WSGIServer(('127.0.0.1', CHAT_SERVER_PORT), Chat().app)
            server.serve_forever()
        except KeyboardInterrupt:
            pass
except IndexError:
    Thread(target=show_chat_forever, daemon=True).start()
    message = ''
    while message != '-q':
        message = input(">")
        requests.post(
            f'http://127.0.0.1:{CHAT_SERVER_PORT}/send', data=message)
print("GOODBYE")
