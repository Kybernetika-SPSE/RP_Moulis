import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID = "35ccd4ae2cab8870610afd219d13b41e84688587"
# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-read-playback-state,user-modify-playback-state"))


# Transfer playback to the Raspberry Pi if music is playing on a different device
sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2XVQdI3m0giGxNrwUhV3yP'])
