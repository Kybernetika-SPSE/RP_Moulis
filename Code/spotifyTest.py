import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import drivers
from datetime import datetime
client_id='5984261fa2d845b3bcf6463bb1df2c97'
client_secret='9c2280c3c0ae4d9392a8870b90165b91'
redirect_uri='http://localhost:8888/callback'

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

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope="user-read-playback-state,user-modify-playback-state"))

#device = sp.devices()[]
DEVICE_ID = "edf62e2b191e93da0bfaee84694b175adbc719f5a"
# Import necessary libraries for communication and display use

print(sp.currently_playing())

display = drivers.Lcd()
cc = drivers.CustomCharacters(display)

# Redefine the default characters:
# Custom caracter #1. Code {0x00}.
cc.char_1_data = ["00010",
                  "00100",
                  "01110",
                  "00001",
                  "01111",
                  "10001",
                  "01111",
				  "00000"]

# Custom caracter #2. Code {0x01}.
cc.char_2_data = ["01010",
                  "00100",
                  "01110",
                  "10001",
                  "11111",
                  "10000",
                  "01110",
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
# Load custom characters data to CG RAM:
cc.load_custom_characters_data()
try:
    print("Writing to display")
    display.lcd_display_extended_string("Pr{0x00}v{0x01} hraje:", 1)  # Write line of text to first line of display
    while True:
        print(sp.currently_playing()['item']['name'])
        hraje = sp.currently_playing()['item']['name']
        long_string(display, hraje, 2)
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()


