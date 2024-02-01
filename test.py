import os
from dotenv import load_dotenv
from SpeechAce import SpeechAce


load_dotenv()
api_key = os.getenv("SPEECHACE_API_KEY")
speechace = SpeechAce(api_key)
speechace.send_premium_request("./audio/test.webm")