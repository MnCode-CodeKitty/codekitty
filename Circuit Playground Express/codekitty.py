import board
from time import sleep
from adafruit_circuitplayground.express import cpx
from pulseio import PWMOut

#
# Setup
#
def online():
    print("--- Code Kitty [CK] v3 online ---")

#
# SERVO FUNCTIONS
#
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


leftServo = PWMOut(board.A3, duty_cycle=4915,  frequency=50)
rightServo = PWMOut(board.A6, duty_cycle=4915,  frequency=50)


def stop():
    leftServo.duty_cycle = angle2dc(90)
    rightServo.duty_cycle = angle2dc(90)


def go(t,spd=5):
    if spd in range(1,7):
       lcspd=(spd*10)+120
       rcspd=80-(spd*10)
       leftServo.duty_cycle = angle2dc(lcspd)
       rightServo.duty_cycle = angle2dc(rcspd)
    else:
        print("[CK] Speed must be between 1 and 6")
    sleep(t)
    stop()


def left(t,spd=5):
    if spd in range(1,7):
       rcspd=80-(spd*10)
       leftServo.duty_cycle = angle2dc(90)
       rightServo.duty_cycle = angle2dc(rcspd)
    else:
        print("[CK] Speed must be between 1 and 6")
    sleep(t)
    stop()


def right(t,spd=5):
    if spd in range(1,7):
       rcspd=(spd*10)+120
       leftServo.duty_cycle = angle2dc(rcspd)
       rightServo.duty_cycle = angle2dc(90)
    else:
        print("[CK] Speed must be between 1 and 6")
    sleep(t)
    stop()


def back(t,spd=5):
    if spd in range(1,7):
       rcspd=(spd*10)+120
       lcspd=80-(spd*10)
       leftServo.duty_cycle = angle2dc(lcspd)
       rightServo.duty_cycle = angle2dc(rcspd)

    else:
        print("[CK] Speed must be between 1 and 6")
    sleep(t)
    stop()


###
### Sound Functions
###
def meow():
    print("[CK] \"Meow\"")
    cpx.play_file("Meow.wav")



def purr():
    print("[CK] *purr*")
    cpx.play_file("Purr.wav")



def beep():
    cpx.play_tone(440,0.3125)


###
### Neopixel functions
###
# Set the brightness of the NeoPixels
# Range is 0.004 to 1.0
cpx.pixels.brightness = 0.1

# Setup the colors
red=(255, 0, 0)
orange=(255, 165, 0)
yellow=(255, 255, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
pink=(255, 192, 203)
purple=(238, 130, 238)
white=(255, 255, 255)
black=(0, 0, 0)

colors=[red,orange,yellow,green,blue,purple,pink,white,yellow,orange]

def rainbow(n=10):
    for i in range(n):
        cpx.pixels[i]=colors[i]
        sleep(0.5)