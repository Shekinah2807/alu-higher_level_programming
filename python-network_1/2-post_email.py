#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request, and displays the body"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
