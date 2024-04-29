#!/usr/bin/python3
"""
a Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
using the packages requests and sys
no need to check arguments passed to the script (number or type
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"
    sys_url = url.format(sys.argv[2], sys.argv[1])

    req = requests.get(sys_url)
    commits = req.json()
    try:
        for n in range(10):
            print("{}: {}".format(
                commits[n].get("sha"),
                commits[n].get("commit").get("author").get("name")))
    except IndexError:
        pass
