import os, sys, collections, spotipy, argparse
from spotipy.oauth2 import SpotifyOAuth

# Spotify authorisation scopes
scope = "user-read-currently-playing user-library-modify"

# Initialise spotipy library
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Get currently playing track and add to saved tracks
try:
  current_track_id = spotify.currently_playing()['item']['id']
  current_track_name = spotify.currently_playing()['item']['name']
except TypeError:
  print('Current track is not available')
else:
  spotify.current_user_saved_tracks_add(tracks=[current_track_id])

print(current_track_name)
