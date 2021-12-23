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
