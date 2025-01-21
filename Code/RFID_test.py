#import serial
from mfrc522 import MFRC522
import utime

#ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
reader = MFRC522()
print("Bring TAG closer...")
print("")
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            print("CARD ID: "+str(card))
utime.sleep_ms(500) 
while True:
    
    tring = ser.read(12) 

    if len(string) == 0:
        print("Please insert a tag")
        continue
    else:
        string = string[1:11] #exclude start x0A and stop x0D bytes

        print(string)