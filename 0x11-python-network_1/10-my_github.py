#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
using basic Authentication with a personal access token as password to access,
to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password
(in this case, a personal access token as password)
using the package requests and sys
no need to check arguments passed to the script (number or type)
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    git_auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=git_auth)
    print(req.json().get("id"))
