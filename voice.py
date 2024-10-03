import pyttsx3
import speech_recognition as sr
import keyboard
import os
import subprocess as sp



from decouple import config
from datetime import datetime
from conv import random_text
from random import choice

engine = pyttsx3.init('sapi5')
engine.setProperty('volume',1.5)
engine.setProperty('rate',185)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


r = sr.Recognizer()

USER = config('USER')
HOSTNAME = config('BOT')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_me():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        greet = (f"Good morning!{USER}")
    elif 12 <= hour < 18:
        greet = (f"Good afternoon!{USER}")
    else:
        greet = (f"Good evening!{USER }")   
    speak(greet)
    speak(f"I am {HOSTNAME}. How may I assist you?")

listening = False

def start_listening():
    global listening
    listening = True
    print("Start listening")

def pause_listening():
    global listening
    listening = False
    print("Listening stopped ")

keyboard.add_hotkey('ctrl + l',start_listening)
keyboard.add_hotkey('ctrl+shift+p',pause_listening)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(query)
        if not 'stop' in query or 'exit' in query:
            speak(choice(random_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6 :
                speak("Good night sir , take care!")
            else:
                speak("Have a good day sir! ")
            exit()    
    except Exception:
        speak("Sorry I coouldn't understand. Can you please repeat that?")
        queri = 'None'
        return queri 
 



if __name__ == '__main__':
    greet_me()
    while True:
        if listening:
            query = take_command().lower()
            if "how are you?" in query:
                speak("I'm absolutely fine sir. What about you")
            elif "open command prompt" in query:
                speak("Opening command prompt")
                os.system('start cmd')
            elif "open camera" in query:
                speak("Opening camera sir")
                sp.run('start microsoft.windows.camera:',shell=True)

            elif "open notepad" in query:
                speak("Opening notepad sir")
                notepad_path = 'C:\Users\vaibh\AppData\Local\Microsoft\WindowsApps\notepad.exe'
                os.startfile(notepad_path)
            elif "open spotify" in query:
                speak("Opening spotify sir")
                spotify_path = 'C:\Users\vaibh\AppData\Local\Microsoft\WindowsApps\Spotify.exe'
                os.startfile(spotify_path)
    
