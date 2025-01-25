#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from time import sleep

DEVICE_ID="35ccd4ae2cab8870610afd219d13b41e84688587"

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())


# Transfer playback to the Raspberry Pi if music is playing on a different device
sp.transfer_playback(device_id=DEVICE_ID, force_play=False)

# Play the spotify track at URI with ID 45vW6Apg3QwawKzBi03rgD (you can swap this for a diff song ID below)
sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2XVQdI3m0giGxNrwUhV3yP'])