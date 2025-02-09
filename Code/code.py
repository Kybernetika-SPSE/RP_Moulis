import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import RPi.GPIO as io
client_id='5984261fa2d845b3bcf6463bb1df2c97'
client_secret='9c2280c3c0ae4d9392a8870b90165b91'
redirect_uri='http://localhost:8888/callback'
DEVICE_ID = "edf62e2b191e93da0bfaee84694b175adbc719f5"

pinA = 2
pinB = 3
pinC = 4
pinD = 17
pin1 = 22
pin2 = 9
pin3 = 10
pin4 = 11
io.setmode(io.BCM)
io.setup(pinA, io.IN, pull_up_down=io.PUD_UP)
io.setup(pinB, io.IN, pull_up_down=io.PUD_UP)
io.setup(pinC, io.IN, pull_up_down=io.PUD_UP)
io.setup(pinD, io.IN, pull_up_down=io.PUD_UP)

io.setup(pin1, io.IN, pull_up_down=io.PUD_DOWN)
io.setup(pin2, io.IN, pull_up_down=io.PUD_DOWN)
io.setup(pin3, io.IN, pull_up_down=io.PUD_DOWN)
io.setup(pin4, io.IN, pull_up_down=io.PUD_DOWN)

def push():
    print(io.input(pin1))
    print(io.HIGH)
# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope="user-read-playback-state,user-modify-playback-state"))

 

# Transfer playback to the Raspberry Pi if music is playing on a different device
sp.transfer_playback(device_id=DEVICE_ID, force_play=True)

while True:
    push()
    #sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2XVQdI3m0giGxNrwUhV3yP'])
    #sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:1Z5EUmtUOtCtjBCCrqJVP7'])

    #sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:6LgJvl0Xdtc73RJ1mmpotq'])
