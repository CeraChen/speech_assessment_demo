import os
import keyboard
import time
from Recorder import Recorder
from dotenv import load_dotenv


START = 0
END = 1



if __name__=="__main__":
    load_dotenv()
    api_key = os.getenv("SPEECHACE_API_KEY")
    recorder = Recorder(api_key)
    
    print("Please press Space to start, or press Esc to exit:")
    while True:
        if keyboard.is_pressed('esc'):
            if recorder.isRecording:
                recorder.beep(END)     
                recorder.stop_recording()
            break
        if keyboard.is_pressed('space'):
            print("-- Space is pressed --")
            recorder.beep(START)
            recorder.start_recording()
            time.sleep(1)
            print("\nPlease press Space to start, or press Esc to exit:")
