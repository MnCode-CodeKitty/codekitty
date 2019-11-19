import board
from time import sleep
from adafruit_circuitplayground.express import cpx
from pulseio import PWMOut

# Setup the note frequencies
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

# set up time signature
wn = 1.5  # adjust this to change tempo of everything
# these notes are fractions of the whole note
# dotted notes are notes * 1.5
hn = wn / 2
qn = wn / 4
en = wn / 8


def note(freq,dur):
    cpx.play_tone(freq,dur)



def march():
    # MEASURE 1
    note(A4,hn)
    note(A4,hn)
    note(A4,hn)
    note(F4,qn)
    note(C4,qn)
    note(A4,hn)
    note(F4,qn)
    note(C4,qn)
    note(A4,wn)
    # MEASURE 2
    note(E5,hn)
    note(E5,hn)
    note(E5,hn)
    note(F5,qn)
    note(C5,qn)
    note(Gs4,hn)
    note(F4,qn)
    note(C4,qn)
    note(A4,wn)
    note(A5,hn)
    note(A4,qn)
    note(A4,qn)
    note(A5,hn)
    note(Gs5,qn)
    note(G5,qn)
    # MEASURE 3
    note(Fs5,qn)
    note(F5,qn)
    note(Fs5,qn)
    note(Bb4,qn)
    note(Eb4,hn)
    note(D4,qn)
    note(Cs4,qn)
    note(C4,qn)
    note(B4,qn)
    note(C4,qn)
    note(F3,qn)
    note(Gs3,hn)
    note(F3,qn)
    note(Gs3,hn)


def hedwig():
    note(E4, qn)
    note(A4, qn)
    note(C5, qn)
    note(B4, qn)
    note(A4, hn)
    note(E5, qn)
    note(D5, hn)
    note(B4, (hn*1.5))
    note(A4, qn)
    note(C5, qn)
    note(B4, qn)
    note(G4, hn)
    note(B4, qn)
    note(E4, (hn*1.5))
    note(E4, qn)
    note(A4, qn)
    note(C5, qn)
    note(B4, qn)
    note(A4, hn)
    note(E5, qn)
    note(G5, hn)
    note(F5, qn)
    note(F5, hn)
    note(C5, qn)
    note(F5, qn)
    note(E5, qn)
    note(E5, qn)
    note(E4, hn)
    note(C5, qn)
    note(A4, (hn*1.5))


def birthday():
    note(D4,en)
    note(D4,en)
    note(E4,qn)
    note(D4,qn)
    note(G4,qn)
    note(F4,hn)
    note(D4,en)
    note(D4,en)
    note(E4,qn)
    note(D4,qn)
    note(A4,qn)
    note(G4,hn)
    note(D4,en)
    note(D4,en)
    note(A4,qn)
    note(B4,qn)
    note(G4,qn)
    note(F4,qn)
    note(E4,qn)
    note(C4,en)
    note(C4,en)
    note(B4,qn)
    note(G4,qn)
    note(A4,qn)
    note(G4,hn)
    
