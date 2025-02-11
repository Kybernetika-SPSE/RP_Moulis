import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
client_id='5984261fa2d845b3bcf6463bb1df2c97'
client_secret='9c2280c3c0ae4d9392a8870b90165b91'
redirect_uri='http://localhost:8888/callback'


# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope="user-read-playback-state,user-modify-playback-state"))

#device = sp.devices()[]
DEVICE_ID = "edf62e2b191e93da0bfaee84694b175adbc719f5a"
# Import necessary libraries for communication and display use

print(sp.currently_playing()['item']['name'])

