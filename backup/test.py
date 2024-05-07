import os
from dotenv import load_dotenv
from SpeechAce import SpeechAce


load_dotenv()
api_key = os.getenv("SPEECHACE_API_KEY")
speechace = SpeechAce(api_key)

dir = "./tmp"
for file in os.listdir(dir):
    print(file)
    path = dir + "/" + file
    speechace.send_premium_request(path)