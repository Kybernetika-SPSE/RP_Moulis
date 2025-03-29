import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
from time import perf_counter
import drivers
from datetime import datetime
import RPi.GPIO as io
import soundcheck as sc
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
# definice funkcí
def get_device(name):
    # získej id zařízení
    device = sp.devices()['devices']
    out = ""
    for i in range(0,len(device)):
        if(device[i]['name']==name):
            out = device[i]['id']
    return out
def long_string_both(display, hraje='', interpret='', play=True, num_cols=16):
    # řeší vypisování údajů na display
    global refresh
    global tic
    global toc
    global new_user
    global was_playing
    if play != was_playing:
        was_playing = play
        refresh = True
    # zjisti posun textu
    if refresh == True:
        refresh = False
        print("refresh")
        tic = perf_counter()
    toc = perf_counter()
    deltaT = toc-tic
    # zjisti progres písničky v %
    progress = min(int(100*sp.current_playback()["progress_ms"])/sp.current_playback()["item"]["duration_ms"],96)
    for j in range(0,16):
                if j >= len(hraje):
                    hraje = hraje+" "
                if j >= len(interpret):
                    interpret = interpret+" "
    
    i = int(deltaT)
    if play:
        if(len(hraje) > num_cols):
            if(i*4<len(hraje)-num_cols):
                display.lcd_display_string(hraje[i*4:num_cols+i*4+1], 1)
            else:  
                display.lcd_display_string(hraje[len(hraje)-num_cols:len(hraje)], 1)
        else:
            display.lcd_display_string(hraje, 1)
        if(i*4>len(hraje)+4):
            refresh = True
        symbol = ["{0x06}","{0x05}","{0x04}","{0x03}","{0x02}","{0x01}"]
        progress_msg = ""
        progress_index = int(progress/6)
        for j in range(16):
            if(j<progress_index):
                progress_msg = progress_msg+"{0x01}"
            if(j==progress_index):
                progress_msg = progress_msg+symbol[int(progress)-(j*6)]
            if(j>progress_index):
                progress_msg = progress_msg+"{0x06}"
             
        display.lcd_display_extended_string(line=2,string = progress_msg)
                
      
    else:
        display.lcd_display_extended_string(line=1,string="Pozastaveno {0x00}   ")
        if(len(interpret) > num_cols):
            if(i*4<len(interpret)-num_cols):
                display.lcd_display_string(interpret[i*4:num_cols+i*4+1], 2)
            else:  
                display.lcd_display_string(interpret[len(interpret)-num_cols:len(interpret)], 2)
        else:
            display.lcd_display_string(interpret, 2)
        if(i*4>len(interpret)+4):
            refresh = True
    return refresh
def diakritika(string=str):
    # převeď českou diakritiku na více friendly text
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
    global cc
    cc = drivers.CustomCharacters(display)

    # Redefine the default characters:
    # Custom caracter #1. Code {0x00}.
    cc.char_1_data = ["00000",
                    "01001",
                    "01001",
                    "01001",
                    "01001",
                    "01001",
                    "01001",
                    "00000"]

    # Custom caracter #2. Code {0x01}.
    cc.char_2_data = ["11111",
                    "11111",
                    "11111",
                    "11111",
                    "11111",
                    "11111",
                    "11111",
                    "11111"]

    # Custom caracter #3. Code {0x02}.
    cc.char_3_data = ["11110",
                    "11110",
                    "11110",
                    "11110",
                    "11110",
                    "11110",
                    "11110",
                    "11110"]

    # Custom caracter #4. Code {0x03}.
    cc.char_4_data = ["11100",
                    "11100",
                    "11100",
                    "11100",
                    "11100",
                    "11100",
                    "11100",
                    "11100"]

    # Custom caracter #5. Code {0x04}.
    cc.char_5_data = ["11000",
                    "11000",
                    "11000",
                    "11000",
                    "11000",
                    "11000",
                    "11000",
                    "11000"]

    # Custom caracter #6. Code {0x05}.
    cc.char_6_data = ["10000",
                    "10000",
                    "10000",
                    "10000",
                    "10000",
                    "10000",
                    "10000",
                    "10000"]

    # Custom caracter #7. Code {0x06}.
    cc.char_7_data = ["00000",
                    "00000",
                    "00000",
                    "00000",
                    "00000",
                    "00000",
                    "00000",
                    "00000"]

    # Custom caracter #8. Code {0x07}.
    cc.char_8_data = ["00110",
                    "10101",
                    "01110",
                    "00100",
                    "01110",
                    "10101",
                    "00110",
                    "00000"]
    cc.load_custom_characters_data()

    
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
                dev = sc.check_connected_devices()
                if(dev):
                    print(dev)
                    io.output(screen, True)
                    display.lcd_display_extended_string(line=1,string="{0x07} Bluetooth")
                    display.lcd_display_string(line=2,string=dev[0])
                    continue
                else:
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