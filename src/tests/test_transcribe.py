import os
from src.transcribe import Transcribe

parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
file_dir = os.path.join(parent_path, r"outputs")
file_path = os.path.join(file_dir, r"result.mp3")

transcribe = Transcribe(language="en")
transcribed_text = transcribe.transcribe_from_audio(file_path)
print(transcribed_text)
