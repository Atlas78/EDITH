import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import wolframalpha
import webbrowser
import ctypes
import psutil
import pyautogui
import os
import sys
import subprocess
import random

chrome_path ='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('E7Q874-J4279K73X4')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Top of the morning to you!")

    elif hour <= 12 and hour < 18:
        speak("Afternoon Boss!")

    else:
        speak("Good Evening!")

    speak("Allow me to introduce Myself, I am EDITH! What can i do for you ?")

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)
