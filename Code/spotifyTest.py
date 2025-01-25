import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

# Change track
sp.start_playback(uris=['spotify:track:6gdLoMygLsgktydTQ71b15'])
