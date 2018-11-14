from time import sleep
import simpleio
import board
#import adafruit_dotstar
import touchio
from analogio import AnalogIn  
import pulseio 

### SOUND FUNCTIONS
def note(notestr,durint):
    # OCTAVE 3
    if (notestr == "C3"):
        notefreq = 131
    elif (notestr == "C#3"):
        notefreq = 139
    elif (notestr == "D3"):
        notefreq = 147
    elif (notestr == "Eb3"):
        notefreq = 156
    elif (notestr == "E3"):
        notefreq = 165
    elif (notestr == "F3"):
        notefreq = 175
    elif (notestr == "F#3"):
        notefreq = 185
    elif (notestr == "G3"):
        notefreq = 196
    elif (notestr == "G#3"):
        notefreq = 208
    elif (notestr == "A3"):
        notefreq = 220
    elif (notestr == "Bb3"):
        notefreq = 233
    elif (notestr == "B3"):
        notefreq = 247
    # OCTAVE 4
    elif (notestr == "C4"):
        notefreq = 262
    elif (notestr == "C#4"):
        notefreq = 277
    elif (notestr == "D4"):
        notefreq = 294
    elif (notestr == "Eb4"):
        notefreq = 293
    elif (notestr == "E4"):
        notefreq = 330
    elif (notestr == "F4"):
        notefreq = 349
    elif (notestr == "F#4"):
        notefreq = 370
    elif (notestr == "G4"):
        notefreq = 392
    elif (notestr == "G#4"):
        notefreq = 415
    elif (notestr == "A4"):
        notefreq = 440
    elif (notestr == "Bb4"):
        notefreq = 466
    elif (notestr == "B4"):
        notefreq = 494
    # OCTAVE 5
    elif (notestr == "C5"):
        notefreq = 523
    elif (notestr == "C#5"):
        notefreq = 554
    elif (notestr == "D5"):
        notefreq = 587
    elif (notestr == "Eb5"):
        notefreq = 622
    elif (notestr == "E5"):
        notefreq = 659
    elif (notestr == "F5"):
        notefreq = 699
    elif (notestr == "F#5"):
        notefreq = 740
    elif (notestr == "G5"):
        notefreq = 784
    elif (notestr == "G#5"):
        notefreq = 831
    elif (notestr == "A5"):
        notefreq = 880
    elif (notestr == "Bb5"):
        notefreq = 932
    elif (notestr == "B5"):
        notefreq = 988
    else:
        print("Invalid note")
        
    if (durint == 1):
        notedur = 1.0
    elif (durint == 2):
        notedur = 0.5
    elif (durint == 4):
        notedur = 0.25
    elif (durint == 8):
        notedur = 0.125
    else:
        print("Invalid note duration")
        
    if (notestr == "rest"):
        sleep(notedur)   

    simpleio.tone(board.D3, notefreq, duration=notedur)
    sleep(notedur/2)
    
def rest(restint):
    if (restint == 1):
        restdur = 1.0
    elif (restint == 2):
        restdur = 0.5
    elif (restint == 4):
        restdur = 0.25
    elif (restint == 8):
        restdur = 0.125
    else:
        print("Invalid rest duration")
    sleep(restdur)
                
def march():
    # First measure
    note("A4",2)
    note("A4",2)
    note("A4",2)
    note("F4",4)
    note("C4",4)
    note("A4",2)
    note("F4",4)
    note("C4",4)
    note("A4",1)
    # Second Measure
    note("E5",2)
    note("E5",2)
    note("E5",2)
    note("F5",4)
    note("C5",4)
    note("G#4",2)
    note("F4",4)
    note("C4",4)
    note("A4",1)
    note("A5",2)
    note("A4",4)
    note("A4",4)
    note("A5",2)
    note("G#5",4)
    note("G5",4)
    # MEASURE 3
    note("F#5",4)
    note("F5",4)
    note("F#5",4)
    note("Bb4",4)
    note("Eb4",2)
    note("D4",4)
    note("C#4",4)
    note("C4",4)
    note("B4",4)
    note("C4",4)
    note("F3",4)
    note("G#3",2)
    note("F3",4)
    note("G#3",2)

    
def beep():
    simpleio.tone(board.A0, 330, duration=0.25)
    
simpleio.tone(board.A0, 1, duration=0)   
    
# SERVO FUNCTIONS

def ms2dc(ms):
    # convert ms to 16 bit duty cycle
    return int(65535 * ms / 20)

def angle2dc(angle):
    # convert 0 to 180 degree angle to 16 bit duty cycle
    ms = 1 + (angle/180)
    return int(65535 * ms / 20)


def unit2dc(speed):
    # convert -1 to 1 to 16 bit duty cycle
    ms = (1 + speed) * 1000 
    return int(65535 * ms / 20)


# Servo runs at 50Hz with the following duty cycle times:
# Full forward: 2.0 ms  -- old 180
# Stop:         1.5 ms  -- old 90   -- 4915
# Full reverse: 1.0 ms  -- old 0

leftServo = pulseio.PWMOut(board.A3, frequency=50)
rightServo = pulseio.PWMOut(board.A6, frequency=50)

def throttle(speed):
    leftServo.duty_cycle = unit2dc(speed)
    rightServo.duty_cycle = unit2dc(speed)

def stop():
    leftServo.duty_cycle = angle2dc(90)
    rightServo.duty_cycle = angle2dc(90)

def go(t,spdtxt="fast"):
    if(spdtxt == 'fast'):
        leftServo.duty_cycle = angle2dc(180)
        rightServo.duty_cycle = angle2dc(180)
    elif(spdtxt == 'slow'):
        leftServo.duty_cycle = angle2dc(140)
        rightServo.duty_cycle = angle2dc(140)
    else:
        print("Invalid Argument")
    sleep(t)
    stop()


    
def left(turn=90):
    if(turn == 90):
        leftServo.duty_cycle = angle2dc(90)
        rightServo.duty_cycle = angle2dc(180)
        sleep(.35)
    elif(turn == 45):
        leftServo.duty_cycle = angle2dc(90)
        rightServo.duty_cycle = angle2dc(140)
        sleep(.6)
    else:
        print("Invalid Argument")
    stop()
    
def right(turn=90):
    if(turn == 90):
        leftServo.duty_cycle = angle2dc(180)
        rightServo.duty_cycle = angle2dc(90)
        sleep(.65)
    elif(turn == 45):
        leftServo.duty_cycle = angle2dc(140)
        rightServo.duty_cycle = angle2dc(90)
        sleep(.5)
    else:
        print("Invalid Argument")
    stop()
    
def back(t,spdtxt="fast"):
    if(spdtxt == 'fast'):
        leftServo.duty_cycle = angle2dc(0)
        rightServo.duty_cycle = angle2dc(0)
    elif(spdtxt == 'slow'):
        leftServo.duty_cycle = angle2dc(50)
        rightServo.duty_cycle = angle2dc(50)
    else:
        print("Invalid Argument")
    sleep(t)
    stop()