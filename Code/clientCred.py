import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
DEVICE_ID = "35ccd4ae2cab8870610afd219d13b41e84688587"
# Spotify Authentication
#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-read-playback-state,user-modify-playback-state"))
sp = spotipy.Spotify(auth=input("Enter auth token"))



# Transfer playback to the Raspberry Pi if music is playing on a different device
artist_uri = 'spotify:artist:4Z8W4fKeB5YxbusRsdQVPb'
results = sp.artist_albums(artist_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])