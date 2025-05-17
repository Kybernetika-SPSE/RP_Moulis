# Modernizace zvukového systému

## 📌 O projektu  
Tento projekt se zaměřuje na modernizaci starého zvukového systému.

## 🛠 Použité technologie  
- **Raspberry Pi Zero 2 W** – hlavní řídicí jednotka  
- **Spotify API** – integrace pro ovládání přehrávání hudby  
- **Raspotify** – umožňuje zařízení fungovat jako Spotify Connect zařízení  
- **Bluetooth Audio** – pro přímé připojení mobilního telefonu  
- **Pulseaudio** – správa zvuku  
- **Spotipy** – Python knihovna pro práci se Spotify  

## ✨ Funkce  
- Přehrávání hudby ze Spotify přes Spotify Connect  
- Možnost připojení přes Bluetooth jako externí reproduktor  
- Zobrazení informací o aktuálně přehrávané skladbě na displeji  
- Více možností zvukového výstupu (3.5 mm Jack, Cinch)  

## 📢 Instalace  
1. **PRaspberry Pi Zero 2 W** s operačním systémem Raspberry Pi OS Lite.  
2. **Potřebné balíčky**:
   ```bash
   sudo apt update && sudo apt install -y curl git python3-pip pulseaudio bluez-tools

- Konfigurace zvukového výstupu: Do souboru /boot/config.txt se přidají následující řádky:
   ```
   dtparam=audio=on
   gpio=12,13,a5
   audio_pwm_mode=2
   dtoverlay=audremap, pins_12_13

- Instalace Raspotify pro přehrávání Spotify:
   ```
   curl -sL https://dtcooper.github.io/raspotify/install.sh | bash

- Konfigurace Bluetooth pro automatické párování:
   ```
   sudo systemctl enable bluetooth
   sudo systemctl start bluetooth


## 🔧 Možná vylepšení
- Integrace baterie pro plně přenosné využití
- Vylepšení grafického rozhraní na displeji
- Snížení šumu na zvukovém výstupu
