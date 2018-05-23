from digitalio import DigitalInOut, Direction, Pull
import audioio
import board
from time import sleep
import simpleio

###### Servos #####  
leftServo = simpleio.Servo(board.A1)
rightServo = simpleio.Servo(board.A2)

# The go() function drives the robot forward.
def go(userTime,*userSpeed):
    if not 1 <= userTime <= 10:
        print ("Time must be between 1 and 10 seconds.")
        exit
    if not userSpeed:
        lSpeed = 0
        rSpeed = 180
    if (userSpeed == 1):
        lSpeed = 70
        rSpeed = 110
    else if (userSpeed == 2):
        lSpeed = 60
        rSpeed = 120 
    else if (userSpeed == 3):
        lSpeed = 40
        rSpeed = 130
    else if (userSpeed == 4):
        lSpeed = 40
        rSpeed = 140
    else if (userSpeed == 5):
        lSpeed = 30
        rSpeed = 150
    else if (userSpeed == 6):
        lSpeed = 20
        rSpeed = 160
    else if (userSpeed == 7):
        lSpeed = 0
        rSpeed = 180
    else:
        print("Speed must be between 1 and 7, where 7 is full speed.")
        exit
    print("Going forward (lSpeed: "+ lSpeed + ", rSpeed: " + rSpeed + ") for " + userTime + " seconds.")
    leftServo.angle = lSpeed
    rightServo.angle = rSpeed
    sleep(userTime)                

#def angleToSpeed(turnAngle):
    # Set the 'speed factor' that the angle is divided by to get the movement time
    #speedFactor = 30
    #baseSpeed = turnAngle/speedFactor

###### Sound Functions #####
PIEZO_PIN = board.D3

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
    simpleio.tone(PIEZO_PIN, notes[note], duration=durations[notetime])

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

