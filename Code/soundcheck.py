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
        return True
    else:
        print("Zvukový výstup nezjištěn.")
        return False

# Spuštění funkce
check_audio_output()

import subprocess

def check_connected_devices():
    try:
        # Získání seznamu zařízení
        output = subprocess.check_output("bluetoothctl devices", shell=True).decode()
        devices = output.strip().split("\n")
        
        if devices:
            print("Kontroluji připojená Bluetooth zařízení...")
            connected_devices = []
            
            for device in devices:
                # Extrahování adresy zařízení z výstupu (formát: Device XX:XX:XX:XX:XX:XX Name)
                device_address = device.split(" ")[1]
                
                # Kontrola informací o zařízení
                info_output = subprocess.check_output(f"bluetoothctl info {device_address}", shell=True).decode()
                if "Connected: yes" in info_output:
                    # Pokud je zařízení připojeno, přidá jej do seznamu
                    device_name = device.split(" ", 2)[2]  # Název zařízení
                    connected_devices.append(f"{device_name} ({device_address})")
            
            if connected_devices:
                print("Aktuálně připojená Bluetooth zařízení:")
                for connected_device in connected_devices:
                    print(connected_device)
                    return connected_device
            else:
                print("Žádná zařízení nejsou aktuálně připojena.")
                return False
        else:
            print("Žádná známá zařízení nebyla nalezena.")
            return False
    
    except subprocess.CalledProcessError as e:
        print(f"Chyba při detekci zařízení: {e}")
        return False

check_connected_devices()