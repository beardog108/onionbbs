#!/usr/bin/env python3

import sys
import os
import time
from threading import Thread

from gevent import pywsgi

import settings
from chatserver import app

try:
    os.mkdir(settings.DATA_DIR)
except FileExistsError:
    pass


USER = "guest"

try:
    if sys.argv[1] == 'daemon':
        try:
            server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
            server.serve_forever()
        except KeyboardInterrupt:
            pass
except IndexError:
    pass
print("GOODBYE")
