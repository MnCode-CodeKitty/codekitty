import board
import simpleio
    
def note(notestr,durint):
    if (notestr == "C4"):
        notefreq = 262
    elif (notestr == "D4"):
        notefreq = 294
    elif (notestr == "E4"):
        notefreq = 330
    elif (notestr == "F4"):
        notefreq = 349
    elif (notestr == "G4"):
        notefreq = 392
    elif (notestr == "A4"):
        notefreq = 440
    elif (notestr == "B4"):
        notefreq = 494
    elif (notestr == "rest")
        notefreq = 0    
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

    simpleio.tone(board.D3, notefreq, duration=notedur)
    
