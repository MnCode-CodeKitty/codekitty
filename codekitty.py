from time import sleep
import touchio
from analogio import AnalogIn  
import pulseio 
from adafruit_circuitplayground.express import cpx

# LED FUNCTIONS

def led(index, color):
    cpx.pixels[index]=color

def rainbow():
    # make this function

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

def leftGo(speed):
    leftServo.duty_cycle = unit2dc(speed)

def rightGo(speed):
    rightServo.duty_cycle = unit2dc(speed)

def throttle(speed):
    leftServo.duty_cycle = unit2dc(speed)
    rightServo.duty_cycle = unit2dc(speed)

def stop():
    leftGo(0)
    rightGo(0)

def go(t,spdtxt="fast"):
    if(spdtxt == 'fast'):
        leftGo(1)
        rightGo(1)
    elif(spdtxt == 'slow'):
        leftGo(.6)
        rightGo(.6)
    else:
        print("Invalid Argument")
    sleep(t)
    stop()


    
def left(turn=90):
    if(turn == 90):
        leftGo(0)
        rightGo(1)
        sleep(.35)
    elif(turn == 45):
        leftGo(0)
        rightGo(.6)
        sleep(.6)
    else:
        print("Invalid Argument")
    stop()
    
def right(turn=90):
    if(turn == 90):
        leftGo(1)
        rightGo(0)
        sleep(.65)
    elif(turn == 45):
        leftGo(.6)
        rightGo(0)
        sleep(.5)
    else:
        print("Invalid Argument")
    stop()
    
def back(t,spdtxt="fast"):
    if(spdtxt == 'fast'):
        leftGo(-1)
        leftGo(-1)
    elif(spdtxt == 'slow'):
        leftGo(-.4)
        rightGo(-.4)
    else:
        print("Invalid Argument")
    sleep(t)
    stop()