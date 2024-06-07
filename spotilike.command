#!/bin/bash

cd PATH_TO_SPOTILIKE_REPO
. setup
source .venv/bin/activate
track_name=$(python3 spotilike.py)
[ $? -eq 0 ] && osascript -e "display notification \"Added currently playing track $track_name to liked songs.\" with title \"SpotiLike\""
