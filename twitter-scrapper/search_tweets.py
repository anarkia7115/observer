#!/usr/bin/env python
# -*- coding: utf-8 -*-

from auth import get_auth
import json

q = "Atlas Shrugged"

count = 100

twitter_api = get_auth()

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']

for _ in range(5):
  print("Length of statuses", len(statuses))
  next_results = ""
  try:
    next_results = search_results['search_metadata']['next_results']
    print("got next results")
  except KeyError as e:
    print("no more results")
    break

  kwargs = dict([kv.split('=') for kv in next_results[1:].split("&")])

  #print( "next_results: ", next_results )
  #print( "kwargs: ", kwargs )

  search_results = twitter_api.search.tweets(**kwargs)
  statuses += search_results['statuses']

print(json.dumps(statuses[1], indent=1))
