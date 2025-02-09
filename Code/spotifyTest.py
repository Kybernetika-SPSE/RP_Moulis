import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
client_id='5984261fa2d845b3bcf6463bb1df2c97'
client_secret='9c2280c3c0ae4d9392a8870b90165b91'
redirect_uri='http://localhost:8888/callback'
DEVICE_ID = "edf62e2b191e93da0bfaee84694b175adbc719f5a"


# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope="user-read-playback-state,user-modify-playback-state"))

 

# Transfer playback to the Raspberry Pi if music is playing on a different device
sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
#sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2XVQdI3m0giGxNrwUhV3yP'])
#sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:1Z5EUmtUOtCtjBCCrqJVP7'])
sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:6LgJvl0Xdtc73RJ1mmpotq'])
