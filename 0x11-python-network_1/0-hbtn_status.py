#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status:
    using the package urllib
    didnt use any packages other than urllib
    using a with statement
"""
import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        url_body = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(url_body)))
        print("\t- content: {}".format(url_body))
        print("\t- utf8 content: {}".format(url_body.decode("utf-8")))
