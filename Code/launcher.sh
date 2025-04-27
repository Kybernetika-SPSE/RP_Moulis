#!/bin/sh
# Provede synchronizaci s kódem na GitHubu
cd /
cd home/mouli/RP_Moulis
sudo git reset --hard origin/main
sudo git pull
sudo git reset --hard origin/main
cd /
# Spustí script na vypisování informací na display
cd home/mouli/RP_Moulis/Code
sudo python spotify.py
cd /