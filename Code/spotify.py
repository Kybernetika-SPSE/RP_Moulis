import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
from time import perf_counter
import drivers
from datetime import datetime
import RPi.GPIO as io
from slib import get_device, long_string_both, diakritika, customchar

sleep(5)
print("started")
# data
client_id='5984261fa2d845b3bcf6463bb1df2c97'
client_secret='9c2280c3c0ae4d9392a8870b90165b91'
redirect_uri='http://localhost:8888/callback'
device_name = 'RPI'
#inicializace
screen = 17
io.setwarnings(False)
io.setmode(io.BCM)
io.setup(screen, io.OUT)
io.setup(26, io.IN, pull_up_down=io.PUD_UP)
display = drivers.Lcd()
    
# systémové proměné
vol_set = False
refresh = True
playing = True
was_playing = True
tic = 0.0
toc = 0.0
interpret = ""
hraje = ""
new_instance = True
new_user = ""


# Autorizace spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope="user-read-playback-state,user-modify-playback-state"))

# získej zařízení
DEVICE_ID = get_device(device_name)
print(DEVICE_ID)

customchar()

# hlavní smyčka, běží dokud je uzemněný pin 26
while not io.input(26):
    try:
        print("Nová smyčka")
        while not io.input(26):
            # pokud je přehrávání nově přesunuto na zařízení, nastav hlasitost na 100%
            if(not vol_set):
                DEVICE_ID = get_device(device_name)
                print(DEVICE_ID)
                if(sp.current_playback()['device']['id']==DEVICE_ID and DEVICE_ID != ""):
                    try:
                        sp.volume(100,DEVICE_ID)
                        vol_set = True
                    except:
                        print("nastavení hlasitosti selhalo")
            # vypni displej pokud není přehrávání aktivní
            if(sp.current_playback()['device']['id']!=DEVICE_ID):
                io.output(screen, False)
                vol_set = False
                print("screen off, due to device != DEVICE_ID")
            else:
                io.output(screen, True)
                print("screen on, due to device == DEVICE_ID")
            
            # vypiš na display jméno přihlášeného uživatele, když se poprvé přihlásí
            if new_instance:
                io.output(screen, True)
                print("on, due to new instance")
                new_instance = False
                new_user = diakritika(sp.current_user()['display_name'])
                new_user = (new_user+"                ")[:16]
                display.lcd_display_string("Prihlasen jako: ", 1)
                display.lcd_display_string(new_user,2)
                sleep(2)
                

            # resetuj scroll displeje pokud začala nová písnička
            if(sp.current_playback()["progress_ms"]<2000):
                refresh = True
                print("New song")
                print(sp.currently_playing()['item']['name'])
                print(sp.currently_playing()['item']['album']['artists'][0]['name'])
            
            # vypiš na displej
            playing = sp.current_playback()['is_playing']    
            interpret = diakritika(sp.currently_playing()['item']['album']['artists'][0]['name'])
            hraje = diakritika(sp.currently_playing()['item']['name'])
            long_string_both(display,hraje,interpret,playing)
    except KeyboardInterrupt:
        break
    except TypeError as Te:
        # chyba když není připojen účet spoitfy
        io.cleanup()
        sleep(1)
        print(Te)
        io.setmode(io.BCM)
        io.setup(screen, io.OUT)
        io.output(screen, False)
        print("off, due to typeerror")
        io.setup(26, io.IN, pull_up_down=io.PUD_UP)
        display.lcd_display_string("Chyba pri init  ",1)
        display.lcd_display_string("Pripojte ucet   ", 2)
        new_instance = True
        sleep(5)
        DEVICE_ID = get_device(device_name)
        print(DEVICE_ID)
        
    except OSError:
        # chyba při špatném připojení kontaků displeje
        sleep(2)
        try:
            io.setmode(io.BCM)
            io.setup(screen, io.OUT)
            io.setup(26, io.IN, pull_up_down=io.PUD_UP)
            display = drivers.Lcd()
            cc.load_custom_characters_data()     
        except:
            print("trying to reconect lcd")
    

# cleanup
print("Cleaning up!")
io.cleanup()
display.lcd_clear()