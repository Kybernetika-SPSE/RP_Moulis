# tento kód je pro testování funkcí spotify na počítači
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
client_id='5984261fa2d845b3bcf6463bb1df2c97'
client_secret='9c2280c3c0ae4d9392a8870b90165b91'
redirect_uri='http://localhost:8888/callback'
device_name = 'RPI'
def diakritika(string=str):
    prevod = [['á','a'],
              ['Á','A'],
              ['č','c'],
              ['Č','C'],
              ['ď','d'],
              ['Ď','D'],
              ['ě','e'],
              ['é','e'],
              ['Ě','E'],
              ['É','E'],
              ['í','i'],
              ['Í','I'],
              ['ň','n'],
              ['Ň','N'],
              ['ó','o'],
              ['Ó','O'],
              ['ř','r'],
              ['Ř','R'],
              ['š','s'],
              ['Š','S'],
              ['ť','t'],
              ['Ť','T'],
              ['ú','u'],
              ['Ú','U'],
              ['ů','u'],
              ['Ů','U'],
              ['ý','y'],
              ['Ý','Y'],
              ['ž','z'],
              ['Ž','Z']]
    for i in range(0,len(prevod)):
        new = ""
        for j in range(0,len(string)):
            if(string[j] == prevod[i][0]):
                new = new+prevod[i][1]
            else:
                new = new+string[j] 
        string = new
    return string
def get_device(name):
    device = sp.devices()['devices']
    #print(device)
    out = ""
    for i in range(0,len(device)):
        if(device[i]['name']==name):
            out = device[i]['id']
    return out
# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope="user-read-playback-state,user-modify-playback-state"))


DEVICE_ID = get_device(device_name)
# Import necessary libraries for communication and display use
#print(DEVICE_ID)
#print(sp.currently_playing()['item']['album']['artists'][0]['name'])
#print(diakritika(sp.currently_playing()['item']['name']))
print("koule")
try:
    print(DEVICE_ID)
    print(sp.current_playback()['is_playing'])
except TypeError as Te:
    if Te == "'NoneType' object is not subscriptable":
        print("koule2")
print(sp.current_playback()["progress_ms"])
print(sp.current_playback()["item"]["duration_ms"])


def long_string_both(display, text1='', text2='', play=True, num_cols=16):
    global refresh
    global tic
    global toc
    global new_user
    lenght = max(len(text1),len(text2))
    if refresh == True:
        refresh = False
        print("refresh")
        tic = perf_counter()
    toc = perf_counter()
    deltaT = toc-tic
    percent = get_percent()
    for j in range(0,16):
                if j >= len(text1):
                    text1 = text1+" "
                if j >= len(text2):
                    text2 = text2+" "
    
    i = int(deltaT)
    if play:
        if(len(text1) > num_cols):
            if(i*4<len(text1)-num_cols):
                display.lcd_display_string(text1[i*4:num_cols+i*4+1], 1)
            else:  
                display.lcd_display_string(text1[len(text1)-num_cols:len(text1)], 1)
        else:
            display.lcd_display_string(text1, 1)

        if(len(text2) > num_cols):    
            if(i*4<len(text2)-num_cols):
                display.lcd_display_string(text2[i*4:num_cols+i*4+1], 2)
            else:  
                display.lcd_display_string(text2[len(text2)-num_cols:len(text2)], 2)
        if(i*4>lenght+4):
            refresh = True
                
        else:
            display.lcd_display_string(text2, 2)    
    else:
        display.lcd_display_extended_string(line=1,string="Pozastaveno {0x01}   ")
        display.lcd_display_string(new_user, 2)
    return refresh
def long_string(display, text='', num_line=1, num_cols=16):
		# dlo
		if len(text) > num_cols:
			display.lcd_display_string(text[:num_cols], num_line)
			sleep(1)
			for i in range(len(text) - num_cols + 1):
				text_to_print = text[i:i+num_cols]
				display.lcd_display_string(text_to_print, num_line)
				sleep(0.2)
			sleep(1)
		else:
			display.lcd_display_string(text, num_line)  

progress = min(int(100*sp.current_playback()["progress_ms"])/sp.current_playback()["item"]["duration_ms"],96)
symbol = ["{0x06}","{0x05}","{0x04}","{0x03}","{0x02}","{0x01}"]
progress_msg = ""
progress_index = int(progress/6)

for j in range(16):
    print(str(j)+", "+str(progress_index))
    if(j<progress_index):
        progress_msg = progress_msg+"{0x01}"
    if(j==progress_index):
        progress_msg = progress_msg+symbol[int(progress)-(j*6)]
    if(j>progress_index):
        progress_msg = progress_msg+"{0x06}"
