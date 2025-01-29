import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
sp_auth=spotipy.oauth2.SpotifyOAuth(scope="user-read-playback-state,user-modify-playback-state", state=state)
#url = sp_auth.get_authorize_url()
auth_token=sp_auth.get_access_token(input())

#{'access_token'  : 'BQD ... qE7K3PBZKB6iZFU3_4p', 
# 'token_type'    : 'Bearer',
# 'expires_in'    : 3600,
# 'refresh_token' : 'AQCOS2Xo ... MK09ry7-a-fl61OwhuO1Q',
# 'scope'         : 'playlist-modify-public user-library-read',
# 'expires_at'    : 1548247835}

sp = spotipy.Spotify(auth=auth_token)

playlists = sp.current_user_playlists(limit=10)
auth=auth_token['access_token']