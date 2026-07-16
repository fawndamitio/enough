# -*- coding: utf-8 -*-
import functools
import os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

DIRECTORY = os.path.dirname(os.path.abspath(__file__))

Handler = functools.partial(SimpleHTTPRequestHandler, directory=DIRECTORY)
ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
