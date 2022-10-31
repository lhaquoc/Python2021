#!/usr/bin/python3

"""
    opensearch.py
    MediaWiki API Demos
    Demo of `Opensearch` module: Search the wiki and obtain
	results in an OpenSearch (http://www.opensearch.org) format
    MIT License
"""

from sqlite3 import DatabaseError
import requests
import json

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "opensearch",
    "namespace": "0",
    "search": "Hampi",
    "limit": "5",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
print(DATA)

with open("wikipedia.json", "w") as outfile:
    json.dump(DATA, outfile)
