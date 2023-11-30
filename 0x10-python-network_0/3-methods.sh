#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept

# Use curl to send a HEAD request (-I option) to the specified URL
# The -s option makes curl operate in silent mode (no progress or error messages)
# The -L option follows redirects
# The response headers are then piped to grep to filter lines containing "Allow"
# The cut command is used to extract the portion after the first space (the actual HTTP methods)
curl -sI -X OPTIONS $1 -L | grep "Allow" | cut -d " " -f2-
