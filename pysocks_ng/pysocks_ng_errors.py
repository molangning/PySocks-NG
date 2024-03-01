#!/usr/bin/env python3

"""

This python modules defines the errors that pysocks-ng-server may raise during execution.

"""


class GeneralProxyError(Exception):
    pass


class ProxyConnectionError(Exception):
    pass


class SOCKS5AuthError(Exception):
    pass


class SOCKS5Error(Exception):
    pass


class SOCKS4Error(Exception):
    pass


class HTTPError(Exception):
    pass
