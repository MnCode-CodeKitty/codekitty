import board
from time import sleep
from adafruit_dotstar import DotStar
from touchio import TouchIn
from analogio import AnalogIn  
from pulseio import PWMOut

# OCTAVE 3 
C3 = 131
Cs3 = 139
D3 = 147
Eb3 = 156
E3 = 165
F3 = 175
Fs3 = 185
G3 = 196
Gs3 = 208
A3 = 220
Bb3 = 233
B3 = 247
# OCTAVE 4
C4 = 262
Cs4 = 277
D4 = 294
Eb4 = 293
E4 = 330
F4 = 349
Fs4 = 370
G4 = 392
Gs4 = 415
A4 = 440
Bb4 = 466
B4 = 494
# OCTAVE 5
C5 = 523
Cs5 = 554
D5 = 587
Eb5 = 622
E5 = 659
F5 = 699
Fs5 = 740
G5 = 784
Gs5 = 831
A5 = 880
Bb5 = 932
B5 = 988


# Setup our piezo object
piezo = PWMOut(board.A3, duty_cycle=0, frequency=440, variable_frequency=True)


def note(note,notedur=4):
    duration=1/notedur
    piezo.frequency = note
    piezo.duty_cycle = 65536 // 2  # On 50%
    sleep(duration)  # On for 1/4 second
    piezo.duty_cycle = 0  # Off
    sleep(0.05)
    
    
def rest(restint):
    rest=1/restint
    sleep(rest)

    
def march():
    # First measure
    note(A4,2)
    note(A4,2)
    note(A4,2)
    note(F4,4)
    note(C4,4)
    note(A4,2)
    note(F4,4)
    note(C4,4)
    note(A4,1)
    # Second Measure
    note(E5,2)
    note(E5,2)
    note(E5,2)
    note(F5,4)
    note(C5,4)
    note(Gs4,2)
    note(F4,4)
    note(C4,4)
    note(A4,1)
    note(A5,2)
    note(A4,4)
    note(A4,4)
    note(A5,2)
    note(Gs5,4)
    note(G5,4)
    # MEASURE 3
    note(Fs5,4)
    note(F5,4)
    note(Fs5,4)
    note(Bb4,4)
    note(Eb4,2)
    note(D4,4)
    note(Cs4,4)
    note(C4,4)
    note(B4,4)
    note(C4,4)
    note(F3,4)
    note(Gs3,2)
    note(F3,4)
    note(Gs3,2)

    
def beep():
    note(E3,4)

    
# SERVO FUNCTIONS

def ms2dc(ms):
    # convert ms to 16 bit duty cycle
    return int(65535 * ms / 20)

def angle2dc(angle):
    # convert 0 to 180 degree angle to 16 bit duty cycle
    ms = 1 + (angle/180)
    return int(65535 * ms / 20)

# Servo runs at 50Hz with the following duty cycle times:
# Full forward: 2.0 ms  -- old 180
# Stop:         1.5 ms  -- old 90   -- 4915
# Full reverse: 1.0 ms  -- old 0

leftServo = PWMOut(board.A2, duty_cycle=4915,  frequency=50)
rightServo = PWMOut(board.A1, duty_cycle=4915,  frequency=50)

def stop():
    leftServo.duty_cycle = angle2dc(90)
    rightServo.duty_cycle = angle2dc(90)

    
def go(t,spdtxt="fast"):
    if(spdtxt == 'fast'):
        leftServo.duty_cycle = angle2dc(0)
        rightServo.duty_cycle = angle2dc(180)
    elif(spdtxt == 'slow'):
        leftServo.duty_cycle = angle2dc(30)
        rightServo.duty_cycle = angle2dc(130)
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
        rightServo.duty_cycle = angle2dc(144)
        sleep(.6)
    else:
        print("Invalid Argument")
    stop()

    
def right(turn=90):
    if(turn == 90):
        leftServo.duty_cycle = angle2dc(0)
        rightServo.duty_cycle = angle2dc(90)
        sleep(.65)
    elif(turn == 45):
        leftServo.duty_cycle = angle2dc(72)
        rightServo.duty_cycle = angle2dc(90)
        sleep(.5)
    else:
        print("Invalid Argument")
    stop()

    
def back(t,spdtxt="fast"):
    if(spdtxt == 'fast'):
        leftServo.duty_cycle = angle2dc(180)
        rightServo.duty_cycle = angle2dc(0)
    elif(spdtxt == 'slow'):
        leftServo.duty_cycle = angle2dc(144)
        rightServo.duty_cycle = angle2dc(72)
    else:
        print("Invalid Argument")
    sleep(t)
    stop()


### TOUCH FUNCTIONS
touch_pad = board.A0
touch = TouchIn(touch_pad)
# touch.value == True if touched


### SENSOR FUNCTIONS
sensor = AnalogIn(board.A4)
# sensor.value is value of sensor input


### LED FUNCTIONS ###
ledlight = DotStar(board.APA102_SCK, board.APA102_MOSI, 1)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return 0, 0, 0
    if pos < 85:
        return int(255 - pos * 3), int(pos * 3), 0
    if pos < 170:
        pos -= 85
        return 0, int(255 - pos * 3), int(pos * 3)
    pos -= 170
    return int(pos * 3), 0, int(255 - (pos * 3))


# Define our colors
red=[255,0,0]
orange=[255,165,0]
yellow=[255,255,0]
green=[0,255,0]
blue=[0,0,255]
purple=[128,0,128]
pink=[255,192,203]
black=[0, 0, 0]
white=[255,255,255]


def led(colorin,br=0.3):
    if(br>1):
        br=1
    ledlight.brightness=br
    ledlight[0]=colorin
        

def rainbow():
    ledlight.brightness = 0.3
    i = 0
    while True:
        i = (i + 1) % 256  # run from 0 to 255
        ledlight.fill(wheel(i))
        sleep(0.01)