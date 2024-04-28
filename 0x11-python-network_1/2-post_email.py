#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8):
The email must be sent in the email variable
using the packages urllib and sys
You don’t need to check arguments passed to the script (number or type)
using the with statement
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    sys_url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")

    request = urllib.request.Request(sys_url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
