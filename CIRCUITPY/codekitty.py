from digitalio import DigitalInOut, Direction, Pull
#import audioio
import board
import time
import simpleio

###### Servos #####  
leftServo = simpleio.Servo(board.A2)
rightServo = simpleio.Servo(board.A1)

def setRange(userInput):
    if 0 <= userInput <= 10:
        fixedInput = userInput/10
        return fixedInput
    else:
        print("Function accepts numbers between 1 and 10.")

def driveRobot(inputTime,lDir,rDir,*inputSpeed):
    # Set the input speed to .8 if they don't enter a speed
    if not inputSpeed:
        speed = 1
    else:
        speed = setRange(inputSpeed)
    # Make sure the time is between 1 and 10
    if not 1 <= inputTime <= 10:
        print ("Time must be a decimal number between 1 and 10.")
        return
    if lDir == 2:
        lSpeed = -speed
    else:
        lSpeed = speed
    if rDir == 2:
        rSpeed = -speed
    else:
        rSpeed = speed
        
    leftServo.angle = lSpeed
    rightServo.angle = rSpeed
    time.sleep(inputTime) 

def go(userTime,*userSpeed):
    driveRobot(userTime,1,1,*userSpeed)

def left(userTime,*userSpeed):
    driveRobot(userTime,2,1,*userSpeed)
    
def right(userTime,*userSpeed):
    driveRobot(userTime,1,2,*userSpeed)

def back(userTime,*userSpeed):
    driveRobot(userTime,2,2,*userSpeed)

def angleToSpeed(turnAngle):
    # Set the 'speed factor' that the angle is divided by to get the movement time
    speedFactor = 30
    baseSpeed = turnAngle/speedFactor

def stop():
    leftServo.angle = 90
    rightServo.angle = 90
    
###### Sound Functions #####
PIEZO_PIN = board.D4

notes = {
    "C4":262,
    "D4":294,
    "E4":330,
    "F4":349,
    "G4":392,
    "A4":440,
    "B4":494
}

durations = {
    "1":1,
    "2":.5,
    "4":.25,
    "8":.125,
    "16":.0625
}

def note(note,notetime):
    simpleio.tone(PIEZO_PIN, notes[note]) #, duration=durations[notetime])

def rest(duration):
    sleep(durations[duration])

def beep(beeps):
    for i in range(beeps):
        note("B4",2)
        rest(2)

###### Meow and Purr #####
#spkrenable = DigitalInOut(board.SPEAKER_ENABLE)
#spkrenable.direction = Direction.OUTPUT
#spkrenable.value = True
#
#def play_file(filename):
#    print("playing file "+filename)
#    f = open(filename, "rb")
#    a = audioio.AudioOut(board.D3, f)
#    a.play()
#    while a.playing:
#        pass
#    print("finished")
#
#def meow():
#    play_file("meow.wav")
#
#def purr():
#    play_fie("purr.wav")
