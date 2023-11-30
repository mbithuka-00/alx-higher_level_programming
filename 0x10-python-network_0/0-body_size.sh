#!/bin/bash

# takes  in url
#sends a request to the url
#displays size of url
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
