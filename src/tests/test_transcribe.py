import os
from src.transcribe import transcribe_from_audio

filepath = "output.mp3"
transcribed_text = transcribe_from_audio(filepath, language="en")
print(transcribed_text)
