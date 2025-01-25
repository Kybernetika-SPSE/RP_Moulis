import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID="35ccd4ae2cab8870610afd219d13b41e84688587"
scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
# Change track
sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2XVQdI3m0giGxNrwUhV3yP'])
