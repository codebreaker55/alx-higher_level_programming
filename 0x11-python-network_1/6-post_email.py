#!/usr/bin/python3
"""
a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.

The email must be sent in the variable email
using the packages requests and sys
no need to error check arguments passed to the script (number or type)
"""
from sys import argv
from requests import post


if __name__ == "__main__":
    sys_url = argv[1]
    email = argv[2]
    req = post(sys_url, data={'email': email})
    print(req.text)
