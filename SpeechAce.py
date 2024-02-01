import json
import requests

class SpeechAce:
    def __init__(self, api_key) -> None:  
        self.api_key = api_key
        self.api_endpoint = "https://api2.speechace.com" 
        self.dialect = "en-us"
        self.user_id = "qef_test"
        
        self.premium_url =  self.api_endpoint + "/api/scoring/speech/v9/json" + \
                    '?' + 'key=' + self.api_key + \
                    '&dialect=' + self.dialect + \
                    '&user_id=' + self.user_id
                    
                    
    def print_result(self, result):
        print("IELTS overall:\t", result["speech_score"]["ielts_score"]["overall"])
        print("Pronunciation:\t", result["speech_score"]["ielts_score"]["pronunciation"])
        print("Fluency:\t", result["speech_score"]["ielts_score"]["fluency"])
        print("Coherence:\t", result["speech_score"]["ielts_score"]["coherence"])
        print("Grammar:\t", result["speech_score"]["ielts_score"]["grammar"])
        print("Vocabulary:\t", result["speech_score"]["ielts_score"]["vocab"])
        print("Transcript:\n", result["speech_score"]["transcript"])
        
        
    def send_premium_request(self, audio_path):
        payload ={
            'include_fluency': '1', 
            'include_intonation': '1',
            'include_speech_score': '1',
            'include_ielts_subscore': '1',
            'include_ielts_feedback': '1',
        }
        audio = open(audio_path, 'rb')
        files = {'user_audio_file': audio}
        response = requests.post(self.premium_url, data=payload, files=files)
        json_result = json.loads(str(response.text))
        result = json.dumps(json_result, indent=4)
        
        splits = audio_path.split("/")
        file_path = "./results/" + splits[-1][:-3] + "json"
        with open(file_path, 'w') as f:
            f.write(result)
        print("Saved result to {}".format(file_path))        
        self.print_result(json_result)
        
        return result