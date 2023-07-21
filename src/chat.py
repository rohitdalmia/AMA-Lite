import google.generativeai as palm
import os

API_KEY = os.getenv("PALM_API_SECRET_KEY")
palm.configure(api_key=API_KEY)


class Chat:
    def __init__(self, message, context, candidates, temperature):
        self.context = context
        self.temperature = temperature
        self.candidates = candidates
        self.response = palm.chat(messages=message, candidate_count=4, context=context, temperature=1)
        print(self.response.last)

    def reply(self, message):
        self.response = self.response.reply(message)
        return self.response.last

    def get_last_reply(self):
        return self.response.last

    def get_chat_history(self):
        return self.response.messages
