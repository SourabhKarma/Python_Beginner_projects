'''
Speech Recognition system

need active internet connection 
pip install speechrecognition
pip install pyaudio

'''
import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Hey !! Say Something !!")
    audio = r.listen(source)
try:
    print("Assistant thinks you said: \n" + r.recognize_google(audio))
except:
    print("Sorry could not recoganize your voice")
