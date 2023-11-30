#!/bin/bash
# sends DELETE request to URL passed as the first argument then displays the body of the response

curl -sX DELETE $1 -L
