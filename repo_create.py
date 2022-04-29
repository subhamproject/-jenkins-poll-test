#!/usr/bin/python

import requests
import os
import json
import argparse

parser = argparse.ArgumentParser(description='GitHub Management')
parser.add_argument("-t", "--token", dest="TOKEN", help="Enter your Github Personal Access Token")
parser.add_argument("-r", "--repo", dest="REPO", help="Enter Github Repo name you want to create")


args = parser.parse_args()
GIT_TOKEN=args.TOKEN
GIT_REPO=args.REPO

GITHUB_API_URL = "https://api.github.com/"
headers = {"Authorization": "token {}".format(GIT_TOKEN)}
data = {"name": "{}".format(GIT_REPO)}

r = requests.post(GITHUB_API_URL +"user/repos" + "", data=json.dumps(data), headers=headers)
print(r)
