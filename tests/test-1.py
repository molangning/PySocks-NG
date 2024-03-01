#!/usr/bin/python3

# Connects to localhost server
# Start with python3 -m http.server

import os
import sys

sys.path.append(os.getcwd())

# import socket from local dir if exist, else import from global
import pysocks_ng as pysocks
from pysocks_ng.custom_logger import get_module_logger 
# 

logger = get_module_logger(__name__)
logger.info('Testing socks function')

s = pysocks.socks_wrapped_socket(pysocks.AF_INET, pysocks.SOCK_STREAM)
s.set_proxy(pysocks.SOCKS5, "127.0.0.1", "1080")
s.connect(("127.0.0.1", 8000))

s.sendall(b"GET / HTTP/1.1\r\nConnection: close\r\n\r\n")

while True:
    chunk = s.recv(4096)

    if not chunk:
        break

    print(chunk, end="")