#!/bin/bash
# script  sends a JSON POST request to a URL  as the first argument, and displays the body of the response.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
