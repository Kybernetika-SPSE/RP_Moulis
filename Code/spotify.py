import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import drivers
from datetime import datetime
import RPi.GPIO as io
client_id='5984261fa2d845b3bcf6463bb1df2c97'
client_secret='9c2280c3c0ae4d9392a8870b90165b91'
redirect_uri='http://localhost:8888/callback'
device_name = 'RPI'
vol_set = 0
refresh = True
playing = True
display_temp = 0
refresh_period = 0,2
screen = 17
interpret = ""
hraje = ""
io.setmode(io.BCM)
io.setup(screen, io.OUT)
io.setup(26, io.IN, pull_up_down=io.PUD_UP)

def get_device(name):
    device = sp.devices()['devices']
    out = ""
    for i in range(0,len(device)):
        if(device[i]['name']==name):
            out = device[i]['id']
    return out
def long_string(display, text='', num_line=1, num_cols=16):
		""" 
		Parameters: (driver, string to print, number of line to print, number of columns of your display)
		Return: This function send to display your scrolling string.
		"""
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


def long_string_both(display, text1='', text2='', play=True, num_cols=16):
    lenght = max(len(text1),len(text2))
    if refresh == True:
        refresh = False
        display_temp = 0
    display_temp += refresh_period
    if play:
        if lenght > num_cols:
            if(display_temp<=1):
                display.lcd_display_string(text1[:num_cols], 1)
                display.lcd_display_string(text2[:num_cols], 2)
            if(display_temp>1 and display_temp <= 1+lenght*refresh_period):
                i = (display_temp - 1)/refresh_period 
                if(len(text1) - num_cols >= i):
                    display.lcd_display_string(text1[i:i+num_cols], 1)
                if(len(text2) - num_cols >= i):
                    display.lcd_display_string(text2[i:i+num_cols], 2)
            if(display_temp>1+lenght*refresh_period+1):
                display_temp = 0    
        else:
            display.lcd_display_string(text1, 1)
            display.lcd_display_string(text2, 2)    


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
def customchar():
    cc = drivers.CustomCharacters(display)

    # Redefine the default characters:
    # Custom caracter #1. Code {0x00}.
    cc.char_1_data = ["00000",
                    "10000",
                    "11100",
                    "11111",
                    "11111",
                    "11100",
                    "10000",
                    "00000"]

    # Custom caracter #2. Code {0x01}.
    cc.char_2_data = ["00000",
                    "01001",
                    "01001",
                    "01001",
                    "01001",
                    "01001",
                    "01001",
                    "00000"]

    # Custom caracter #3. Code {0x02}.
    cc.char_3_data = ["10001",
                    "10001",
                    "10001",
                    "11111",
                    "11111",
                    "11111",
                    "11111",
                    "11111"]

    # Custom caracter #4. Code {0x03}.
    cc.char_4_data = ["11111",
                    "11011",
                    "10001",
                    "10001",
                    "10001",
                    "10001",
                    "11011",
                    "11111"]

    # Custom caracter #5. Code {0x04}.
    cc.char_5_data = ["00000",
                    "00000",
                    "11011",
                    "11011",
                    "00000",
                    "10001",
                    "01110",
                    "00000"]

    # Custom caracter #6. Code {0x05}.
    cc.char_6_data = ["01010",
                    "11111",
                    "11111",
                    "01110",
                    "00100",
                    "00000",
                    "00000",
                    "00000"]

    # Custom caracter #7. Code {0x06}.
    cc.char_7_data = ["11111",
                    "11011",
                    "10001",
                    "10101",
                    "10101",
                    "10101",
                    "11011",
                    "11111"]

    # Custom caracter #8. Code {0x07}.
    cc.char_8_data = ["11111",
                    "10001",
                    "11111",
                    "00000",
                    "00000",
                    "11111",
                    "10001",
                    "11111"]
    cc.load_custom_characters_data()

display = drivers.Lcd()

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope="user-read-playback-state,user-modify-playback-state"))

#device = sp.devices()[]
DEVICE_ID = get_device(device_name)
print(DEVICE_ID)
#if(DEVICE_ID!=""):
    #sp.transfer_playback(DEVICE_ID,True)
    #sp.volume(100,DEVICE_ID)


#uncoment when using custom characters
customchar()


while not io.input(26):
    try:
        print("Writing to display")
        #display.lcd_display_extended_string("Pr{0x00}v{0x01} hraje:", 1)  # Write line of text to first line of display
        while not io.input(26):
            if(sp.current_playback()['device']['id']==DEVICE_ID):
                if(vol_set == 0):
                    sp.volume(100,DEVICE_ID)
                    vol_set = 1
                io.output(screen, True)
            else:
                io.output(screen, False)
                vol_set = 0
                
            
            print(sp.currently_playing()['item']['name'])
            print(sp.currently_playing()['item']['album']['artists'][0]['name'])
            
            if(interpret!=diakritika(sp.currently_playing()['item']['album']['artists'][0]['name']) or hraje!=diakritika(sp.currently_playing()['item']['name'])):
                refresh = True
                print("New song")

            playing = sp.current_playback()['is_playing']

            interpret = diakritika(sp.currently_playing()['item']['album']['artists'][0]['name'])
            hraje = diakritika(sp.currently_playing()['item']['name'])
            for i in range(0,16):
                if i >= len(interpret):
                    interpret = interpret+" "
                if i >= len(hraje):
                    hraje = hraje+" "
            long_string_both(display,interpret,hraje,playing)
    except KeyboardInterrupt:
        # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        
        break
    except OSError:
        sleep(2)
        try:
            display = drivers.Lcd()
            cc.load_custom_characters_data()     
        except:
            print("trying to reconect lcd")
    


print("Cleaning up!")
io.cleanup()
display.lcd_clear()