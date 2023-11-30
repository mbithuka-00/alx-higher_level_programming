#!/bin/bash
# takes in url, sends GET request,  and displays 

curl -sX GET $1 -L
