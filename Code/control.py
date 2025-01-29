import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID = "35ccd4ae2cab8870610afd219d13b41e84688587"
sp = spotipy.Spotify()
#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-read-playback-state,user-modify-playback-state"))
while(what!="end"):
    print("play; pause, next, end")
    what = input()

    if(what=="pause"):
        sp.pause_playback(device_id=DEVICE_ID)

    if(what=="next"):
        sp.next_track(device_id=DEVICE_ID)

    if(what=="play"):
        sp.start_playback(device_id=DEVICE_ID)
