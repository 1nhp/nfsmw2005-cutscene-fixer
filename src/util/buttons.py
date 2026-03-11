from .playsound import playsound
import threading

def click():
    threading.Thread(target=lambda: playsound("decide.wav")).start()