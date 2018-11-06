import simpleio
import board 
from time import sleep

def noter(notestr,dur):
    # OCTAVE 3
    timebase = .125
    notedur = timebase * dur
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
    elif (notestr == "Gb3"):
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
    elif (notestr == "D#4"):
        notefreq = 293
    elif (notestr == "Eb4"):
        notefreq = 293
    elif (notestr == "E4"):
        notefreq = 330
    elif (notestr == "F4"):
        notefreq = 349
    elif (notestr == "F#4"):
        notefreq = 370
    elif (notestr == "Gb4"):
        notefreq = 370
    elif (notestr == "G4"):
        notefreq = 392
    elif (notestr == "G#4"):
        notefreq = 415
    elif (notestr == "A4"):
        notefreq = 440
    elif (notestr == "A#4"):
        notefreq = 466
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
    elif (notestr == "rest"):
        notefreq = 1
    else:
        print("Invalid note")  

    simpleio.tone(board.D3, notefreq, duration=notedur)
    sleep(.1)
    
def march2():
    # 
    noter("G3",4)
    noter("G3",4)
    noter("G3",4)
    noter("Eb3",3)
    noter("Bb4",1)
    #
    noter("G3",4)
    noter("Eb3",3)
    noter("Bb4",1)
    noter("G3",8)
    # 
    noter("D4",4)
    noter("D4",4)
    noter("D4",4)
    noter("Eb4",3)
    noter("C4",1)
    #
    noter("G#3",4)
    noter("Eb3",3)
    noter("Bb4",1)
    noter("A4",8)
    #
    noter("G4",4)
    noter("A4",3)
    noter("A4",1)
    noter("G4",4)
    noter("Gb4",3)
    noter("F4",1)
    # 
    noter("E4",1)
    noter("D#4",1)
    noter("E4",2)
    noter("rest",2)
    noter("A#4",2)
    noter("C#4",4)
    noter("C4",3)
    noter("B4",1)
    #
    noter("Bb4",1)
    noter("A4",1)
    noter("Bb4",2)
    noter("rest",2)
    noter("E3",2)
    noter("Gb3",4)
    noter("E3",3)
    noter("Gb3",1)
    #
    noter("Bb4",4)
    noter("G3",3)
    noter("Bb4",1)
    noter("D4",8)