import pyttsx3
import PyPDF2

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
#rate = speaker.getProperty('rate')
speaker.setProperty("rate", 150)
speaker.say('i am alive I dont want it to go really slow just slow enough to be easy for a non native speaker to understand')

speaker.runAndWait()
#book  = open("","rb")
