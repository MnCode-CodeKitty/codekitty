import time
import simpleio
import board
import adafruit_dotstar


 
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
        ledlight[0]=(255, 0, 0)
    elif(color=="green"):
        ledlight[0]=(0, 255, 0)
    elif(color=="blue"):
        ledlight[0]=(0, 0, 255)
    elif(color=="off"):
        ledlight[0]=(0, 0, 0)
        

def rainbow():
    ledlight.brightness = 0.3
    i = 0
    while True:
        i = (i + 1) % 256  # run from 0 to 255
        ledlight.fill(wheel(i))
        time.sleep(0.01)
    
# SERVO FUNCTIONS
leftServo = simpleio.Servo(board.A2)
rightServo = simpleio.Servo(board.A1)

def go(t,spdtxt="fast"):
    if(spdtxt == 'fast'):
        leftServo.angle = 0
        rightServo.angle = 180
    elif(spdtxt == 'slow'):
        leftServo.angle = 60
        rightServo.angle = 120
    else:
        print("Invalid Argument")
    time.sleep(t)
    leftServo.angle = 90
    rightServo.angle = 90
    
def left(turn=90):
    if(turn == 90):
        leftServo.angle = 90
        rightServo.angle = 0
        time.sleep(1)
    elif(turn == 45):
        leftServo.angle = 90
        rightServo.angle = 60
        time.sleep(3)
    else:
        print("Invalid Argument")
    leftServo.angle = 90
    rightServo.angle = 90
    
def back(t,spdtxt="fast"):
    if(spdtxt == 'fast'):
        leftServo.angle = 0
        rightServo.angle = 180
    elif(spdtxt == 'slow'):
        leftServo.angle = 60
        rightServo.angle = 120
    else:
        print("Invalid Argument")
    time.sleep(t)
    leftServo.angle = 90
    rightServo.angle = 90