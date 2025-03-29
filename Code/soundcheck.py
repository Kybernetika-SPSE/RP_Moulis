import sounddevice as sd
import numpy as np

# Nastavení parametrů
DURATION = 2  # Délka snímání v sekundách
SAMPLERATE = 44100  # Vzorkovací frekvence
CHANNELS = 2  # Stereo výstup

def check_audio_output():
    print("Kontroluji zvuk...")

    # Záznam signálu po dobu určitého intervalu
    recording = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=CHANNELS, dtype='float64')
    sd.wait()  # Čeká na dokončení záznamu

    # Analýza
    signal_level = np.max(np.abs(recording))  # Maximální amplituda
    if signal_level > 0.01:  # Limitní hodnota
        print(f"Zvukový výstup detekován! Úroveň signálu: {signal_level}")
    else:
        print("Zvukový výstup nezjištěn.")

# Spuštění funkce
check_audio_output()

import dbus

def get_bluetooth_metadata():
    bus = dbus.SystemBus()
    proxy = bus.get_object("org.bluez", "/org/bluez/hci0/dev_B8_27_EB_F1_58_9B/player0")
    interface = dbus.Interface(proxy, "org.bluez.MediaPlayer1")
    properties = interface.GetAll("org.bluez.MediaPlayer1")
    print("Název skladby:", properties.get("Track", {}).get("Title", "Neznámý"))
    print("Interpret:", properties.get("Track", {}).get("Artist", "Neznámý"))
    print("Album:", properties.get("Track", {}).get("Album", "Neznámý"))

get_bluetooth_metadata()