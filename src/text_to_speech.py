import os
import requests

ELEVEN_LABS_API_KEY = os.getenv(key="ELEVEN_LABS_API_KEY")
CHUNK_SIZE = 1024


def get_voices():
    url = "https://api.elevenlabs.io/v1/voices"
    headers = {
        "xi-api-key": ELEVEN_LABS_API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()["voices"]


def generate_audio(text, output_path, voice_char_name):
    voices = get_voices()
    voice_name = ""
    voice_id = ""
    for voice in voices:
        if voice["name"] == voice_char_name:
            voice_name = voice["name"]
            voice_id = voice["voice_id"]
    url = "https://api.elevenlabs.io/v1/text-to-speech/{}".format(voice_id)
    headers = {
        "Content-Type": "application/json",
        "xi-api-key": ELEVEN_LABS_API_KEY
    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }
    print(url)
    response = requests.post(url, json=data, headers=headers)

    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
    return output_path
