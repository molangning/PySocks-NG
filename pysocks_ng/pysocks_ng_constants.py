#!/usr/bin/env python3

"""

This python module defines the constants used in pysocks-ng

"""

PROXY_TYPE_SOCKS4 = SOCKS4 = 1
PROXY_TYPE_SOCKS5 = SOCKS5 = 2
PROXY_TYPE_HTTP = HTTP = 3

PROXY_TYPES = {"SOCKS4": SOCKS4, "SOCKS5": SOCKS5, "HTTP": HTTP}
PRINTABLE_PROXY_TYPES = dict(zip(PROXY_TYPES.values(), PROXY_TYPES.keys()))
DEFAULT_PORTS = {SOCKS4: 1080, SOCKS5: 1080, HTTP: 8080}

SOCKS4_ERRORS = {
    0x5B: "Request rejected or failed",
    0x5C: ("Request rejected because SOCKS server cannot connect to identd on"
           " the client"),
    0x5D: ("Request rejected because the client program and identd report"
           " different user-ids")
}

SOCKS5_STATUSES = {
    b'\x00': "Connection Succeeded",
    b'\x01': "General SOCKS server failure",
    b'\x02': "Connection not allowed by ruleset",
    b'\x03': "Network unreachable",
    b'\x04': "Host unreachable",
    b'\x05': "Connection refused",
    b'\x06': "TTL expired",
    b'\x07': "Command not supported, or protocol error",
    b'\x08': "Address type not supported"
}

RSV = b"\x00"
SOCKS5_VER = b"\x05"

# Command cmds that clients can send

CONNECT_CMD = b"\x01"
BIND_CMD = b"\x02"
UDP_ASSOCIATE_CMD = b"\x03"

# Constants for authentication methods

NO_AUTH = b"\x00"
GSSAPI_AUTH = b"\x01"
USER_PASS_AUTH = b"\x02"
NO_SUPPORTED_AUTH = b"\xFF"

# Constants for username password authentication

USER_PASS_VER = b"\x01"
USER_PASS_AUTH_SUCCESS = b"\x00"
USER_PASS_AUTH_FAIL	= b"\x01"

# Reply codes

REPLY_SUCCESS = b"\x00"
REPLY_GENERAL_FAILURE = b"\x01"
REPLY_CONNECTION_NOT_ALLOWED= b"\x02"
REPLY_NETWORK_UNREACHABLE = b"\x03"
REPLY_HOST_UNREACHABLE = b"\x04"
REPLY_CONNECTION_REFUSED = b"\x05"
REPLY_TTL_EXPIRED = b"\x06"
REPLY_COMMAND_UNSUPPORTED = b"\x07"
REPLY_ADDRESS_UNSUPPORTED = b"\x08"

# ATYP fields

ATYPIPV4 = b"\x01"
ATYPDOMAIN = b"\x03"
ATYPIPV6 = b"\x04"