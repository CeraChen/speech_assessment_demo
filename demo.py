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
    
    task_assigned = True
    if task_assigned:
        task_type = "describe-image" # One of these three types: describe-image, retell-lecture, answer-question
        task_context = open("./task_context.txt", "r", encoding="utf-8").read() # As the ONLY scoring basis
        assert len(task_context) <= 1024, "The task context should not exceed 1024 characters, but it currently contains {} characters. Please REDUCE its length.".format(len(task_context))
    
        recorder.assign_task(task_type, task_context)
        print(task_context)
        print("A {} task has been assigned, please give your answer according to this task.".format(task_type))
    
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
