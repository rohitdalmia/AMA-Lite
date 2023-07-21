import os
from speechmatics.models import ConnectionSettings
from speechmatics.batch_client import BatchClient
from httpx import HTTPStatusError


AUTH_TOKEN = os.getenv(key="SPEECHMATICS_API_KEY")
settings = ConnectionSettings(
    url="https://asr.api.speechmatics.com/v2",
    auth_token=AUTH_TOKEN
)


def transcribe_from_audio(filepath, language = "en"):
    conf = {
        "type": "transcription",
        "transcription_config": {
            "language": language,
            "enable_entities": True
        }
    }
    # opening the client using a context manager
    with BatchClient(settings) as client:
        try:
            job_id = client.submit_job(audio=filepath, transcription_config=conf)
            print(f"job {job_id} submitted successfully, waiting for response")
            transcript = client.wait_for_completion(job_id=job_id, transcription_format="txt")
            return transcript
        except HTTPStatusError:
            print("Invalid API key - Check your AUTH_TOKEN at the top of the code!")
            return
