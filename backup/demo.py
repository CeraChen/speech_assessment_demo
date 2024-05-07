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
    task_type = 'describe-image' # One of these three types: describe-image, retell-lecture, answer-question
    task_context = "You are a senior college student. Liu Hong is a new student in your department. You are aware \
                    that Liu Hong has been under a lot of stress with study and is on treatment for depression. This \
                    morning Liu Hong asked you to have a read at one of her final essays and offer her some feedback. \
                    You read the essay and noticed it was badly written, with chunks of paragraphs plagiarised from \
                    other sources. Liu Hong told you she had to submit this paper tomorrow morning. You decide to \
                    send her a voice message to talk about her essay." 
    # As the ONLY scoring basis
    if task_assigned:
        recorder.assign_task(task_type, task_context)
        print(recorder.task_context)
        print("A **{}** task has been assigned, please give your answer according to this task.".format(task_type))
    
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
