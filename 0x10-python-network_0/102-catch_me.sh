#!/bin/bash
# Script to catch the server's special response
curl -sLX PUT "0.0.0.0:5000/catch_me" -H "Origin: You got me!" -d "user_id=98" --data-urlencode "email=test@example.com"
