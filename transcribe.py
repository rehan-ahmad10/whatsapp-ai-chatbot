# =========== Modules & Imports ===========
from groq import Groq

from api import groqapi

client = Groq(api_key=groqapi)


# =========== Functions ===========

def transcribe_voice_notes(list2, chat_text):
    n = 0
    for note in list2:
        voice_text = ""
        with open(f"{note}.ogg", "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=file,
                language="en",
                model="whisper-large-v3"
            )
            voice_text += "[ ] Other : "
            voice_text += transcription.text
            chat_text = chat_text.replace(f"Voice note {n}", voice_text)
            n += 1

    return chat_text