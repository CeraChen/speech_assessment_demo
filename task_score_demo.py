import os
import keyboard
import time
from Recorder import Recorder
from SpeechAce import SpeechAce
from dotenv import load_dotenv


START = 0
END = 1



if __name__=="__main__":
    load_dotenv()
    api_key = os.getenv("SPEECHACE_API_KEY")
    recorder = Recorder(api_key, False)
    speechace = SpeechAce(api_key)
    
    task_assigned = True    
    task_type = "describe-image" # One of these three types: describe-image, retell-lecture, answer-question
    context_dir = "./context"
   
    print("=== Task Score ===")
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
            audio_path = recorder.start_recording()
            
            print("Audio file {} is being assessed now.".format(audio_path))
            for id, context_file in enumerate(os.listdir(context_dir)):
                task_context = open(context_dir + "/" + context_file, "r", encoding="utf-8").read() # As the ONLY scoring basis
                assert len(task_context) <= 1024, "The task context should not exceed 1024 characters, but it currently contains {} characters. Please REDUCE its length.".format(len(task_context))
                # print("Context of Task {}:".format(id+1))
                # print(task_context)
                speechace.send_premium_task_request(audio_path, task_type, task_context, context_file, id)
            
            time.sleep(1)
            print("\nPlease press Space to start, or press Esc to exit:")
