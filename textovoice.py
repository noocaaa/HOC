# --------------------------------------------------------------------------------------------------------------------------
#  TEXT TO VOICE
#	We would use an external library. To use it, we put on the terminal: pip3 install gTTS pyttsx3 playsound
# --------------------------------------------------------------------------------------------------------------------------

import gtts
from playsound import playsound

# the text from google, lang="XX" for other languages 
tts = gtts.gTTS("Hello world") 

# save 
tts.save("hello.mp3")

# reproduce it
playsound("hello.mp3")
