import pyttsx3
from decouple import config
from datetime import datetime


engine = pyttsx3.init('sapi5')
engine.setProperty('volume',1.5)
engine.setProperty('rate',185)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


USER = config("USER")
HOSTNAME = config('BOT')

def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_me():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        greet = "Good morning!"
    elif 12 <= hour < 18:
        greet = "Good afternoon!"
    else:
        greet = "Good evening!"
    
    speak(greet)
    speak("Say 'Hello wakeup' to start.")

if __name__ == '__main__':
    greet_me()
    speak("Hii, I am your virtual assistant")
