import os.path
from src.text_to_speech import generate_audio

output_path = "src/tests/output.mp3"
text_to_audio = generate_audio("hello this is rakesh from microsoft and I am here to scam you hahahaha", output_path, voice_char_name="Josh")
