print("Code Kitty v2.2 online")
from codekitty import *
from time import sleep
while True:
    if(sensor.value < 6000):
        led("purple")
        beep()
    else:
        led("red")
    
    if(touch.value == True):
        go(.2)
        led("blue")
        sleep(.1)
        