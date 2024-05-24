import os
import keyboard
import time
import pandas as pd
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
    columns = ["audio"]
    results = {}
    
    task_assigned = True    
    task_type = "describe-image" # One of these three types: describe-image, retell-lecture, answer-question
    context_dir = "./context"
    
   
    print("=== Task Score ===")
    # count = 0
    for audio_name in os.listdir("./score_task_speech"):  
        # count += 1
        # if count > 1:
        #     break
        audio_path = "./score_task_speech/" + audio_name
        results[audio_name] = {}
                  
        print("Audio file {} is being assessed now.".format(audio_path))
        for id, context_file in enumerate(os.listdir(context_dir)):
            rubric_name = context_file.split(".")[0]
            if rubric_name not in columns:
                columns.append(rubric_name)
                
            task_context = open(context_dir + "/" + context_file, "r", encoding="utf-8").read() # As the ONLY scoring basis
            assert len(task_context) <= 1024, "The task context should not exceed 1024 characters, but it currently contains {} characters. Please REDUCE its length.".format(len(task_context))
            score = speechace.send_premium_task_request(audio_path, task_type, task_context, context_file, id)
            
            results[audio_name][rubric_name] = score

    summary = pd.DataFrame(columns=columns)
    for key, value in results.items():
        value["audio"] = key
        summary = pd.concat([summary, pd.DataFrame([value])], ignore_index=True)
    print(summary)