import os
from speechmatics.models import ConnectionSettings
from speechmatics.batch_client import BatchClient
from httpx import HTTPStatusError


class Transcribe:
    def __init__(self, language="en"):
        self.auth_token = os.getenv(key="SPEECHMATICS_API_KEY")
        self.settings = ConnectionSettings(
                            url="https://asr.api.speechmatics.com/v2",
                            auth_token=self.auth_token
                        )
        self.conf = {
            "type": "transcription",
            "transcription_config": {
                "language": language,
                "enable_entities": True
            }
        }

    def transcribe_from_audio(self, filepath):
        # opening the client using a context manager
        with BatchClient(self.settings) as client:
            try:
                job_id = client.submit_job(audio=filepath, transcription_config=self.conf)
                print(f"job {job_id} submitted successfully, waiting for response")
                transcript = client.wait_for_completion(job_id=job_id, transcription_format="txt")
                return transcript
            except HTTPStatusError:
                raise Exception("Error in transcribing audio, please try again")

