# SpotiLike

Like the currently playing track in Spotify.

## Purpose

I got annoyed with having to switch to the Spotify app, then to find the currently playing track, then to find the button to add the track to my liked songs. I wanted to be able to quickly start typing something into Spotlight Search to like the currently playing track without having to switch apps, spaces, etc.

This is a fairly quick and dirty solution, but it works to achieve what I wanted on macOS.

Please feel free to fork this and improve on it.

## Requirements

* A [Spotify](https://www.spotify.com/) account.
* [Python 3](https://www.python.org/).

## Setup

1. Log in to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) with your Spotify account.
1. Choose CREATE AN APP, give it a name and description, tick the "I understand" box, and choose CREATE.
1. Make a note of the Client ID and Client Secret.
1. Choose EDIT SETTINGS and add `http://127.0.0.1:9090` under Redirect URIs, then choose SAVE.
1. Copy _setup\_template_ to _setup_, then edit _setup_ and add the Client ID and Client Secret for your newly created Spotify app.
1. (Assuming you're using Bash or similar) import the setup environment variables with `. setup`.
2. Create virtualenv: `python3 -m venv .venv` if not previously done, then `source .venv/bin/activate`.
3. Install requirements if needed: `python3 -m pip install -r requirements.txt`.

## Usage

Run application:

    python3 spotilike.py

## Making available from Spotlight Search

Create a file called _spotilike.command_ in a location indexed by Spotlight, e.g. _~/Documents_ or wherever else you like, with the following contents (replacing `PATH_TO_LOCATION_OF_COMMAND` with the location of _spotilike.command_, e.g. _/Users/bob/Documents_ or wherever you're putting it:

```
#!/bin/bash

cd PATH_TO_LOCATION_OF_COMMAND
. setup
source .venv/bin/activate
python3 spotilike.py
```

Make the file executable: `chmod 755 spotilike.command`.

Give your Mac a minute for the Spotlight index to update, then you should be able to bring up Spotlight Search and type "spotilike.command", and it should show up in the results. After you've used it a few times it should appear quickly after you start typing it.