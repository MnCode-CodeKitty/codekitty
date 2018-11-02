from time import sleep
import board
from pulseio import PWMOut
from adafruit_dotstar import DotStar
from adafruit_motor import servo
from touchio import TouchIn
from analogio import AnalogIn   

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

    buzzer = pulseio.PWMOut(board.D3, variable_frequency=True)
    NOTEON = 2**15
    NOTEOFF = 0
    buzzer.frequency = notefreq
    buzzer.duty_cycle = NOTEON  # 32768 value is 50% duty cycle, a square wave.
    sleep(notedur)
    buzzer.duty_cycle = NOTEOFF
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
    simpleio.tone(board.D3, 330, duration=0.25)
    
simpleio.tone(board.D3, 1, duration=0)   
    
# SERVO FUNCTIONS

# create a PWMOut object on Pin A2.
pwmA2 = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
pwmA1 = pulseio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
 
# Create a servo object, my_servo.
leftServo = servo.Servo(pwmA2)
rightServo = servo.Servo(pwmA1)
#leftServo = simpleio.Servo(board.A2)
#rightServo = simpleio.Servo(board.A1)

def go(t,spdtxt="fast"):
    if(spdtxt == 'fast'):
        leftServo.angle = 0
        rightServo.angle = 180
    elif(spdtxt == 'slow'):
        leftServo.angle = 50
        rightServo.angle = 120
    else:
        print("Invalid Argument")
    sleep(t)
    leftServo.angle = 90
    rightServo.angle = 90

def stop():
    leftServo.angle = 90
    rightServo.angle = 90
    
def left(turn=90):
    if(turn == 90):
        leftServo.angle = 90
        rightServo.angle = 180
        sleep(.35)
    elif(turn == 45):
        leftServo.angle = 90
        rightServo.angle = 120
        sleep(.6)
    else:
        print("Invalid Argument")
    leftServo.angle = 90
    rightServo.angle = 90
    
def right(turn=90):
    if(turn == 90):
        leftServo.angle = 0
        rightServo.angle = 90
        sleep(.65)
    elif(turn == 45):
        leftServo.angle = 60
        rightServo.angle = 90
        sleep(.5)
    else:
        print("Invalid Argument")
    leftServo.angle = 90
    rightServo.angle = 90
    
def back(t,spdtxt="fast"):
    if(spdtxt == 'fast'):
        leftServo.angle = 180
        rightServo.angle = 0
    elif(spdtxt == 'slow'):
        leftServo.angle = 120
        rightServo.angle = 60
    else:
        print("Invalid Argument")
    sleep(t)
    leftServo.angle = 90
    rightServo.angle = 90

### TOUCH FUNCTIONS
touch_pad = board.A0
touch = touchio.TouchIn(touch_pad)
# touch.value == True if touched

### SENSOR FUNCTIONS
sensor = AnalogIn(board.A4)
# sensor.value is value of sensor input

### LED FUNCTIONS ###
ledlight = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)

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


def led(color,br=0.3):
    if(br>1):
        br=1
    ledlight.brightness=br
    if(color=="red"):
        ledlight[0]=(255,0,0)
    elif(color=="orange"):
        ledlight[0]=(255,165,0)
    elif(color=="yellow"):
        ledlight[0]=(255,255,0)
    elif(color=="green"):
        ledlight[0]=(0,255,0)
    elif(color=="blue"):
        ledlight[0]=(0,0,255)
    elif(color=="purple"):
        ledlight[0]=(128,0,128)
    elif(color=="pink"):
        ledlight[0]=(255,192,203)
    elif(color=="off"):
        ledlight[0]=(0, 0, 0)
        

def rainbow():
    ledlight.brightness = 0.3
    i = 0
    while True:
        i = (i + 1) % 256  # run from 0 to 255
        ledlight.fill(wheel(i))
        sleep(0.01)