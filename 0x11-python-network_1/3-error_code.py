#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
manage urllib.error.HTTPError exceptions,
and print: Error code: followed by the HTTP status code
using the packages urllib and sys
no need to check arguments passed to the script (number or type)
using the with statement
"""
import sys
from urllib import request, error


if __name__ == "__main__":
    sys_url = sys.argv[1]
    try:
        with request.urlopen(sys_url) as resp:
            print(resp.read().decode('utf-8'))
    except error.HTTPError as eror:
        print("Error code: {}".format(eror.status))
