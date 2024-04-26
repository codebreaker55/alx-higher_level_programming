#!/bin/bash
# a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response a variable email must be sent with the value test@gmail.com, and variable subject must be sent with the value I will always be here for PLD, using curl
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
