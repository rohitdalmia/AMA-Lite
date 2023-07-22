import os
from src.text_to_speech import TextToSpeech

parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
output_dir = os.path.join(parent_path, r"outputs")
output_path = os.path.join(output_dir, r"result.mp3")
print(output_path)

os.makedirs(output_dir, exist_ok=True)
text2speech = TextToSpeech(voice_char_name="Josh")
text2speech.generate_audio(text="hello there, how can I be of assistance?", output_path=output_path)
