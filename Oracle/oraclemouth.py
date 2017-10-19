from oracleheart import *
from gtts import gTTS

#Not working yet
finnish = 'fi'
english = 'en'
default = english
accent = default

def say_in_gtts(text_to_say):
    tts = gTTS(text=text_to_say, lang=accent, slow=False)
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")


def say(text_to_say):
    print(text_to_say)
    say_in_gtts(text_to_say)

def say0(text_to_say):
    say_in_gtts(text_to_say)
