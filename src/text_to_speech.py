import os
import requests


class TextToSpeech:
    def __init__(self, voice_char_name):
        self.api_key = os.getenv(key="ELEVEN_LABS_API_KEY")
        self.chunk_size = 1024
        self.voice_char_name = voice_char_name

    def get_voices(self):
        url = "https://api.elevenlabs.io/v1/voices"
        headers = {
            "xi-api-key": self.api_key
        }
        response = requests.get(url, headers=headers)
        return response.json()["voices"]

    def generate_audio(self, text, output_path):
        if len(text) == 0:
            raise Exception("Empty messages cannot be transcribed")

        voices = self.get_voices()
        voice_id = ""
        for voice in voices:
            if voice["name"] == self.voice_char_name:
                voice_id = voice["voice_id"]
        if len(voice_id) == 0:
            raise Exception(f"Voice with input name not found")

        url = "https://api.elevenlabs.io/v1/text-to-speech/{}".format(voice_id)
        headers = {
            "Content-Type": "application/json",
            "xi-api-key": self.api_key
        }

        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }
        response = requests.post(url, json=data, headers=headers)

        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=self.chunk_size):
                if chunk:
                    f.write(chunk)
        return output_path
