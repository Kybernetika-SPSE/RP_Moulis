#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home
cd /
cd home/mouli/RP_Moulis
sudo git reset --hard origin/main
sudo git pull
sudo git reset --hard origin/main
cd /
cd home/mouli/RP_Moulis/Code
sudo python spotify.py
cd /