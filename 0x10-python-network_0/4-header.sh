#!/bin/bash
# Sends a GET request to a URL, includes a header variable, and displays the body of the response
curl -s "$1" -H "X-School-User-Id: 98"
