#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
using the packages urllib and sys
The value of this variable is different for each request
no need to check arguments passed to the script (number or type)
using a with statement
"""
import sys
import urllib.request


if __name__ == "__main__":
    sys_url = sys.argv[1]
    with urllib.request.urlopen(sys_url) as response:
        print(response.headers["X-Request-Id"])
