#!/usr/bin/python3
"""
Module to send a request to a URL and display the value of the X-Request-Id header
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = urllib.request.urlopen(url)
    x_request_id = response.getheader('X-Request-Id')
    print(x_request_id)
    response.close()
