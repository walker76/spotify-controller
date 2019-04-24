#!/usr/bin/env python

import os
import sys
import spotipy
import webbrowser
import spotipy.util as util

spotify = spotipy.Spotify()

username=sys.argv[1]

try:
	token = util.prompt_for_user_token(username)
except:
	# os.remove(f".cache-{username}")
	token = util.prompt_for_user_token(username)

spotifyObject = spotipy.Spotify(auth=token)

print(spotifyObject)


