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

album = {11:'spotify:track:2XVQdI3m0giGxNrwUhV3yP',
         12:'spotify:track:1Z5EUmtUOtCtjBCCrqJVP7',
         13:'spotify:track:6LgJvl0Xdtc73RJ1mmpotq',
         14:'',
         21:'',
         22:'',
         23:'',
         24:'',
         31:'',
         32:'',
         33:'',
         34:'',
         41:'',
         42:'',
         43:'',
         44:'',}


def push():
    inx = 0
    inx += io.input(pin1)*1
    inx += io.input(pin2)*2
    inx += io.input(pin3)*3
    inx += io.input(pin4)*4

    if(inx>4):
        return 0
    if(inx==0):
        return 0
    inx += io.input(pinA)*-10+10
    inx += io.input(pinB)*-20+20
    inx += io.input(pinC)*-30+30
    inx += io.input(pinD)*-40+40    

    if(inx<11):
        return 0
    if(inx>44):
        return 0
    print(inx)
    return inx
    
# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope="user-read-playback-state,user-modify-playback-state"))

 

# Transfer playback to the Raspberry Pi if music is playing on a different device
sp.transfer_playback(device_id=DEVICE_ID, force_play=True)

while True:
    num = push()
    if(io.input(pin1)==1):
        num = 11
    if(io.input(pin2)==1):
        num = 12
    if(io.input(pin3)==1):
        num = 13        
    if(io.input(pin4)==1):
        num = 14
    

    
    if(num != 0 and album[num]!=''):
        sp.start_playback(device_id=DEVICE_ID, uris=[album[num]])
        print(num)
        print(album[num])
        sleep(5)
        
