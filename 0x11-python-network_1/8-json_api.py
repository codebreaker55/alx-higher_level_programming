#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
-Display Not a valid JSON if the JSON is invalid
-Display No result if the JSON is empty
"""
from requests import post
from sys import argv

if __name__ == '__main__':

    sys_url = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1] if len(argv) >= 2 else ""}
    response = post(sys_url, data)

    sys_type = response.headers['content-type']

    if sys_type == 'application/json':
        res = response.json()
        _id = res.get('id')
        name = res.get('name')
        if (res != {} and _id and name):
            print("[{}] {}".format(_id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
