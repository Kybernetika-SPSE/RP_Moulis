import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

import spotipy.until as until

DEVICE_ID="35ccd4ae2cab8870610afd219d13b41e84688587"
CLIENT_ID="5984261fa2d845b3bcf6463bb1df2c97"
CLIENT_SECRET="9c2280c3c0ae4d9392a8870b90165b91"


    
sp = spotipy.Spotify(auth=0ueqzovsyyh02tfkyiygz2j59)


# Transfer playback to the Raspberry Pi if music is playing on a different device
sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2XVQdI3m0giGxNrwUhV3yP'])
