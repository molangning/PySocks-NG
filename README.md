### PySocks-NG

# Heavy refactoring ahead!

Major changes will be made to the project in order to improve usability. Try not to use this until I am done with my improvements. However, if you need to use this fork, Just beware of the future breakages down the road.

Oh, and about everything is untested until I can do up tests.

-----------------

PySocks-NG is a fork of [PySocks](https://github.com/Anorov/PySocks) which is in turn a fork of [SocksiPy](http://socksipy.sourceforge.net/)

Py-Socks-NG include fixes and pull requests from the original project as the owner has disappeared into the oblivion and has not committed any code for [Almost 3 years, from Mid 2020 to 2023](https://github.com/Anorov). As such, quality fixes are not included in them,

Acts as a drop-in replacement to the socket module. Seamlessly configure SOCKS proxies for any socket object by calling `socket_object.set_proxy()`.

----------------

### Features

* SOCKS proxy client for Python 2.7 and 3.4+
* TCP supported, UDP mostly supported (issues may occur in some edge cases)
* HTTP proxy client included but not supported or recommended (you should use requests', or your HTTP client's, own HTTP proxy interface)
* urllib2 handler included, but not supported. `pip install` / `setup.py install` will automatically install the `sockshandler` module.

-----------------

### Installation

    pip3 install pysocks-ng

Or download the tarball / `git clone` and...

    python setup.py install

These will install both the `socks` and `sockshandler` modules.

Alternatively, include just `socks.py` in your project.

-----------------

### Proxying HTTP Traffic

We highly recommend using the [requests](https://2.python-requests.org/en/master/) library for proxying HTTP traffic with SOCKS or HTTP proxies. It uses PySocks under the hood.

```python
requests.get(url, proxies={"http": "socks5://proxyhostname:9050", "https": "socks5://proxyhostname:9050"})
```

PySocks has an option for HTTP proxies, but it only supports CONNECT-based HTTP proxies, and in general we recommend using your HTTP client's native proxy support (such as requests' `proxies` keyword argument) rather than PySocks'.

If you absolutely must, you can use the urllib2 handler in sockshandler.py, but it's not supported (and won't work for non-CONNECT-based HTTP proxies, as stated above).

-----------------

### Usage

-----------------

Opening a socket with socks5 proxy.

```python
import socks

s = socks.socksocket() # Same API as socket.socket in the standard lib

s.set_proxy(socks.SOCKS5, "localhost") # SOCKS4 and SOCKS5 use port 1080 by default
# Or
s.set_proxy(socks.SOCKS4, "localhost", 4444)
# Or
s.set_proxy(socks.HTTP, "5.5.5.5", 8888)

# Can be treated like a regular socket object
s.connect(("www.somesite.com", 80))
s.sendall("GET / HTTP/1.1 ...")
print(s.recv(4096))
```

-----------------

#### Monkeypatching
-----------------

To monkeypatch the entire standard library with a localhost proxy:

```python
import urllib2
import socket
import socks

socks.set_default_proxy(socks.SOCKS5, "localhost")
socket.socket = socks.socksocket
```

Note that monkeypatching may not work for all standard modules or for all third party modules, and generally isn't recommended. Monkeypatching is usually an anti-pattern in Python.

PROBLEMS
---------

Please open a GitHub issue at https://github.com/molangning/PySocks-NG
