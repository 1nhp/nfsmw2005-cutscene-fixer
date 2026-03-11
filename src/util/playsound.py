import playsound3
import os
import threading
import time

def playsound(file, loop=False, loop_delay=0):
    filename = os.path.join("./", "audio", file)

    def play_loop():
        while True:
            playsound3.playsound(filename, block=False)  # block here is fine, it's in its own thread
            if loop_delay > 0:
                time.sleep(loop_delay)
            if not loop:
                break

    threading.Thread(target=play_loop, daemon=True).start()