import os
from dotenv import load_dotenv
from joke_api.joke import joke
from audio.text_to_audio import text_to_speech


load_dotenv()

url = os.getenv("JOKE_URL")
text = joke(url)

text_to_speech(text)
