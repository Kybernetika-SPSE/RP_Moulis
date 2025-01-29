import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import spotipy.util as util

USERNAME = '0ueqzovsyyh02tfkyiygz2j59' #your spotify username
CLIENT_ID = '5984261fa2d845b3bcf6463bb1df2c97'#set at your developer account
CLIENT_SECRET = '9c2280c3c0ae4d9392a8870b90165b91' #set at your developer account
REDIRECT_URI = 'http://localhost:8888/callback' #set at your developer account, usually "http://localhost:8000"
SCOPE = 'user-read-playback-state,user-modify-playback-state' # or else

token = util.prompt_for_user_token(username = USERNAME, 
                                   scope = SCOPE, 
                                   client_id = CLIENT_ID, 
                                   client_secret = CLIENT_SECRET, 
                                   redirect_uri = REDIRECT_URI)

if token:
   sp = spotipy.Spotify(auth=token)
   print(sp)
   # dig your api