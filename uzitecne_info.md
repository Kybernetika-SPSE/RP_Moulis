Raspotify je program který řeší přehrávání hudby na zařízení. ten funguje, ale díky němu se dá zařízení ovládat pouze z aplikace v mobilu nebo počítači

Spotipy je knihovna do pythonu, která posílá příkazy přes API na ovládání přehrávání

tyhle dvě věci nejsou vlastně ani nijak provázaný, jedno řeší audio a druhý ovládání

takže by teoreticky mělo spotipy fungovat i libovolného jiného zařízení (jenom mě to doteď nenapadlo vyzkoušet) 

raspotify/spotify connect
---
tohle funguje, jenom pro případný test

jméno na spotify connect: Hifi obyvak

mělo by to normálně fungovat jako reproduktor na spotify connect, potřebuje akorát připojení k internetu

ze stejné sítě se na to dá napojit, jenom trvá pár minut než se raspotify (přes který tohle jede) probere a začne normálně fungovat

problém
---
aktuálně problém je v autorizaci knihovny. když se pustí:
`sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-read-playback-state,user-modify-playback-state")) `

tak to vytvoří autorizační url kde se dá přihlásit do spotify
když url překopíruju do počítače, kde už jsem přihlášen, tak se autorizuje a přesměruje na ten redirect uri, a tam končím

(ještě záleží kde se to pustí, v cmd se otevře lynx, ze kterého dokážu vykopírovat url ale jinak nemá žádný možnosti jak s tím pracovat.

ve VNC přes thonny se otevře defaultní prohlížeč (viz níže) kde se dá přihlásit, nebo překopírovat url a vložit přesměrovanou)
pokud chápu správně tak si ta knihovna následně nedokáže vzít data z toho prohlížeče, ale nevím


```client: '5984261fa2d845b3bcf6463bb1df2c97'

secret: '9c2280c3c0ae4d9392a8870b90165b91'

id zařízení: '35ccd4ae2cab8870610afd219d13b41e84688587'

redirect uri: 'http://localhost:8888/callback'
```


test na požadavek songu
(funky town)

`spotify:track:2XVQdI3m0giGxNrwUhV3yP`



příkazy:
```
git pull
git reset --hard origin/main

cd /home/mouli/RP/RP_Moulis

sudo nano etc/environment
	export SPOTIPY_CLIENT_ID='5984261fa2d845b3bcf6463bb1df2c97'
	export SPOTIPY_CLIENT_SECRET='9c2280c3c0ae4d9392a8870b90165b91'
	export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'

sudo update-alternatives --config x-www-browser
	#puffin (4) - rozběhne se a funguje celkem pěkně ale nejsem si jistý jestli mu nechybí nějaký funkce od normálního prohlížeče
	#Firefox (3) - jakože naběhne asi tak po 15 minutách ale dál je nepoužitelnej


#tohle by mělo získat access token, vycházím tu přímo z dokumentace spotify, a nepoužívá to tu spotipy knihovnu
#zatím to nikam nevedlo, nepřišel jsem na to jak narvat ten access token do toho python kódu
#šlo by zajít i dál ale to by už vyžadovalo js a ten neumím a rpi ho momentálně taky neumí

curl -X POST "https://accounts.spotify.com/api/token" \
     	-H "Content-Type: application/x-www-form-urlencoded" \
     	-d "grant_type=client_credentials&client_id=5984261fa2d845b3bcf6463bb1df2c97&client_secret=9c2280c3c0ae4d9392a8870b90165b91"
```
