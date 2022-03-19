#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id

"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    req = requests.get('https://api.github.com/users/{}'.format(sys.argv[1]),
                     auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(req.json().get('id'))

