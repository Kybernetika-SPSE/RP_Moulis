import subprocess

def check_connected_devices():
    try:
        # Získání seznamu zařízení
        output = subprocess.check_output("bluetoothctl devices", shell=True).decode()
        devices = output.strip().split("\n")
        print(devices)
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

