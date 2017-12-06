#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter
import os

def oauth_req(url, http_method="GET", post_body="", http_headers=None):

  ck = os.environ.get("CONSUMER_KEY")
  cs = os.environ.get("CONSUMER_SECRET")
  at = os.environ.get("ACCESS_TOKEN")
  ats = os.environ.get("ACCESS_TOKEN_SECRET")

  consumer = oauth2.Consumer(key=ck, secret=cs)
  token = oauth2.Token(key=at, secret=ats)
  client = oauth2.Client(consumer, token)
  resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
  return content

def get_auth():

  ck = os.environ.get("CONSUMER_KEY")
  cs = os.environ.get("CONSUMER_SECRET")
  at = os.environ.get("ACCESS_TOKEN")
  ats = os.environ.get("ACCESS_TOKEN_SECRET")

  auth = twitter.oauth.OAuth(at, ats, ck, cs)

  twitter_api = twitter.Twitter(auth=auth)

  return twitter_api

