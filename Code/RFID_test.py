from machine import UART, Pin
import time

uart = UART(1, 9600)
uart.init(9600, bits=8, parity=None, stop=1, rx=15, tx=14)

while True:
    b = uart.read()
    if not b == None:
        print(b)