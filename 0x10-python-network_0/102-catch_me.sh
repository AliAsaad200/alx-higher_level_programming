#!/bin/bash
# Makes a request to cause the server to respond with "You got me!"
curl -s "0.0.0.0:5000/catch_me" -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" -L
