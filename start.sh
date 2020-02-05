#!/usr/bin/bash

tor -f torrc &
tcpserver 127.0.0.1 8889 onionbbs/__init__.py &
onionbbs/__init__.py daemon