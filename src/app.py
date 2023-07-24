from flask import Flask, session, request, render_template, jsonify, send_file, abort
import uuid
import os
import shutil

from chat import Chat
# from transcribe import Transcribe
from text_to_speech import TextToSpeech

# transcribeObj = Transcribe()
text2speechObj = TextToSpeech(voice_char_name="Josh")
chatObj = Chat(message=" ", candidates=4, context="you are a helpful assistant", temperature=0.75)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


# @app.route('/transcribe', methods=['POST'])
# def transcribe():
#     print("running transcribe")
#     if 'file' not in request.files:
#         abort(400)
#     file = request.files['file']
#     upload_dir = "uploads"
#     recording_name = "{}.mp3".format(uuid.uuid4())
#     recording_path = "uploads/{}".format(recording_name)
#     os.makedirs(upload_dir, exist_ok=True)
#     file.save(recording_path)
#     transcription = transcribeObj.transcribe_from_audio(recording_path)
#     print(transcription)
#     return jsonify({"text": transcription})


@app.route('/ask', methods=['POST'])
def ask():
    print("running ask")
    message = request.get_json(force=True).get("message", "")
    reply = chatObj.reply(message=message)
    output_dir = "outputs"
    reply_file = "{}.mp3".format(uuid.uuid4())
    reply_path = "outputs/{}".format(reply_file)
    os.makedirs(output_dir, exist_ok=True)
    text2speechObj.generate_audio(text=reply, output_path=reply_path)
    return jsonify({"text": reply, "audio": "/listen/{}".format(reply_file)})


@app.route('/listen/<filename>')
def listen(filename):
    print("running listen")
    return send_file("outputs/{}".format(filename), mimetype="audio/mp3", as_attachment=False)


@app.errorhandler(400)
def file_not_found():
    return render_template("400.html"), 400


app.run(debug=True)
