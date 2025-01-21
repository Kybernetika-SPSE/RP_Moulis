import serial

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

while True:
    string = ser.read(12) 

    if len(string) == 0:
        print("Please insert a tag")
        continue
    else:
        string = string[1:11] #exclude start x0A and stop x0D bytes

        print(string)