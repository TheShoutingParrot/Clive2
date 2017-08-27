from oracleheart import *
from espeak import espeak

def say(text):
    print(text)
    espeak.synth(text)

def say0(text):
    espeak.synth(text)
