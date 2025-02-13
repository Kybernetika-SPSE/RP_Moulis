import RPi.GPIO as io
import time

io.setmode(io.BCM)
io.setup(17,io.OUT)
while True:
    io.output(17,0)
    time.sleep(1)
    io.output(17,1)
    time.sleep(1)