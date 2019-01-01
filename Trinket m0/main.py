print("Code Kitty v2.2 Booting")
from codekitty import *
from time import sleep
from random import randint

print("Code Kitty v2.2 Ready!")
beep()

def randTurn():
    td=randint(1,2)
    if(td==1):
        print("[CK] LEFT(90)") 
        left(90)
    elif(td==2):
        print("[CK] RIGHT(90)") 
        right(90)

while True:
    print("[CK] STOP")
    sleep(.5)
    while(touch.value==False):
        led(red)
    note(C4,8)
    note(E4,4)
    note(G4,2)
    turns=0
    while(touch.value==False):
        if(sensor.value<14000):
            print("[CK] STOP")
            stop()
            sleep(2)
            print("[CK] BACK")
            led(blue)
            back(.5,"slow")
            sleep(2)
            randTurn()
            turns += 1
            sleep(2)
            if(turns==3):
                led(yellow)
                print("[CK] Frustration level 3!")
                note(D3,2)
                print("[CK] Getting out of here!")
                back(1)
                sleep(1)
                left(90)
                sleep(1)
                left(90)
                sleep(1)
        else:
            print("[CK] GO")
            led(green)
            go(.375,"slow")
            sleep(1)
            turns=0
    note(E5,8)
    note(A4,8)
    note(C5,4)
    note(G5,4)
    note(A4,2)    