#!/usr/bin/python3
"""Script that takes GitHub credentials (username and personal access token) and uses the GitHub API to display your id"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))
    data = response.json()
    
    if response.status_code == 200:
        print(data['id'])
    else:
        print(None)
