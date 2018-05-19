# codekitty
The Code Kitty v2.0 CircuitPython Module

Usage: from codekitty import *

Functions:
----------
- go(seconds)       Go forward for (seconds) seconds
- back(seconds)     Go backward for (seconds) seconds
- left(degrees)     Turn (degrees) to the left
- right(degrees)    Turn (degrees) to the right

- tail(on/off)      Turns the Tail LED on or off
- blink(times)      Blinks the Tail LED (times)

- beep()            Plays one beep on the builtin speaker
- risingBeep()      Plays three beeps of rising pitch
- melody()          Plays a short melody
- note(NOTE,Time)   Plays a note (like C4,etc or REST) for Time
- meow()            Plays meow.wav
- purr()            Plays purr.wav

- sensor()          Reads a voltage between 0 and 1000 from a sensor
