import os
from dotenv import load_dotenv
from SpeechAce import SpeechAce



if __name__=="__main__":
    load_dotenv()
    api_key = os.getenv("SPEECHACE_API_KEY")
    speechace = SpeechAce(api_key)
    task_type = "describe-image" # One of these three types: describe-image, retell-lecture, answer-question
    task_context = open("./task_context.txt", "r", encoding="utf-8").read() # As the ONLY scoring basis
    assert len(task_context) <= 1024, "The task context should not exceed 1024 characters, but it currently contains {} characters. Please REDUCE its length.".format(len(task_context))
        
    dir = "./score_task_speech"
    for file in os.listdir(dir):
        print("Audio file {file} is being assessed now.")
        print(task_context)
        path = dir + "/" + file
        speechace.send_premium_task_request(path, task_type, task_context)