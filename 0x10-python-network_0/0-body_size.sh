#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
# The size must be displayed in bytes, and have to use curl
curl -s "$1" | wc -c
