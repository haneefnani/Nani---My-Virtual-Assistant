import datetime
import pyautogui
import getpass
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import sys

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 185)
password = "hello"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('Good Morning!')
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak('Good Evening!')
    speak('I am Friday')
    speak('How can i help you?')
    #speak('I am virtual assistant designed to Help you!!')

def passWord():
    n = getpass.getpass('>> ')

    if n == password:
        print("The password is ended with status (DONE)\n")

    else:
        print("The code is exited with status (NOT DONE)\nSorry you can't able to use jarvis")
        time.sleep(5)
        quit()

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\\scr\\screenshot.png") #path where screenshot will be saved
        
def takeCommand():
    '''
    It takes microphone input from user and returns a string

    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print(e)

        print('Say that again please.....')
        return 'None'
    return query


if __name__ == '__main__':
    passWord
    wishMe()
    while True:
        query =  takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'open music' in query:
            path = 'C:\\Users\\haneef\\Pictures\\shareit'
            os.startfile()
        elif "take screenshot" in query:
            speak("taking screenshot")
            screenshot()
        elif 'quit' in query:
            sys.exit()
        else:
            speak("sorry the command you entered is not stisfied")
