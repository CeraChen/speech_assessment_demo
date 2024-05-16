import os
from dotenv import load_dotenv
from SpeechAce import SpeechAce



if __name__=="__main__":
    load_dotenv()
    api_key = os.getenv("SPEECHACE_API_KEY")
    speechace = SpeechAce(api_key)
    task_type = "describe-image" # One of these three types: describe-image, retell-lecture, answer-question
     
    dir = "./score_task_speech"
    context_dir = "./context/question_plus_rubrics"
    for file in os.listdir(dir):
        # if "bad3" not in file:
        #     continue
        print("Audio file {} is being assessed now.".format(file))
        for context_file in os.listdir(context_dir):
            task_context = open(context_dir + "/" + context_file, "r", encoding="utf-8").read() # As the ONLY scoring basis
            assert len(task_context) <= 1024, "The task context should not exceed 1024 characters, but it currently contains {} characters. Please REDUCE its length.".format(len(task_context))
       
            print("\n")
            print(context_file)
            # print(task_context)
            path = dir + "/" + file
            speechace.send_premium_task_request(path, task_type, task_context)