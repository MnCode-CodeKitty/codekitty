from digitalio import DigitalInOut, Direction, Pull
import audioio
import board
import time
import simpleio 

###### Servos #####  
servo = simpleio.Servo(board.A2)

###### Meow and Purr #####
spkrenable = DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = Direction.OUTPUT
spkrenable.value = True

def play_file(filename):
    print("playing file "+filename)
    f = open(filename, "rb")
    a = audioio.AudioOut(board.A0, f)
    a.play()
    while a.playing:
        pass
    print("finished")

def meow():
    play_file("meow.wav")

def purr():
    play_fie("purr.wav")

