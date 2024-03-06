#!/usr/bin/python3

import struct

import socket as _socket
from _socket import *

from pysocks_ng.custom_logger import get_module_logger 
from pysocks_ng.constants import *
from pysocks_ng.errors import *

# Those imports are horrible, do we have an alternative?

# Create logger
logger = get_module_logger(__name__)

class socks_wrapped_socket(_socket.socket):

    """Wrapped socket for socks5 connections"""

    def __init__(self, family=_socket.AF_INET, type=_socket.SOCK_STREAM,
                 proto=0, *args, **kwargs):

        if type not in (_socket.SOCK_STREAM, _socket.SOCK_DGRAM):
            logger.debug("Got an invalid family, throwing error")
            raise _socket.error("PySocks-ng does not support non stream/datagram sockets")

        super().__init__(family, type, proto, *args, **kwargs)

        self.socks_handler = None

    def set_proxy(self, *args, **kwargs):
        self.socks_handler = socks_handler(*args, **kwargs)

    def connect(self, dest_pair):
        
        if len(dest_pair) != 2:
            raise TypeError("Address must be a host port pair")

        dest_addr, dest_port = dest_pair

        try:
            _socket.inet_pton(self.family, dest_addr)

        except _socket.error as e:
            logger.debug("Got illegal ip for family, rethrowing error...")
            raise e
        
        logger.debug("Trying to connect to %s:%i", dest_addr, dest_port)
        super().connect(dest_pair)

class socks_handler():

    "Socks handler for connections"

    def __init__(self, socks_proto, socks_dest, socks_port = 0, rdns = True, username = None, password = None):
        
        self.rdns = rdns
        self.username = username
        self.password = password

        if socks_proto != SOCKS5:
            raise GeneralProxyError("Unimplemented protocol, only socks5 is supported")

        # Socket getaddrinfo returns ipv6 if addr is ipv6, and vice versa

        family, type, proto, _, socksaddr = _socket.getaddrinfo(socks_dest, socks_port, proto=_socket.IPPROTO_TCP)[0]

        self.socks_conn = _socket.socket(family, type, proto)
        logger.debug("Connecting to socks proxy")

        self.socks_conn.connect(socksaddr)
        logger.debug("Connected successfully")

        self.socks5_negotiate()

    def socks5_negotiate(self):

        available_methods = [NO_AUTH]

        # What do we have?
        if self.username is not None and self.password is not None:

            # We have username and password! Tell server that we prefer that.
            available_methods.insert(0, USER_PASS_AUTH)

        # We build the payload
        payload = SOCKS5_VER + struct.pack("!B", len(available_methods)) + b"".join(available_methods)

        # And send it!
        self.socks_conn.send(payload)

        logger.debug("Sent auth req payload")

        server_resp = self.socks_conn.recv(2)

        choosen_method = server_resp[1:2]

        # Is it no auth?
        if choosen_method == NO_AUTH:

            # Great! We can now continue
            self.socks5_request()
            logger.debug("Using no auth for authentication")

        else:

            # Did not implement that yet
            raise GeneralProxyError("Server wants a non implemented authentication method.")
    
    def socks5_request(self):
        pass        

