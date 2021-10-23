import os
from dotenv import load_dotenv
from joke_api.joke import joke
from gtts import gTTS

load_dotenv()
url = os.getenv("JOKE_URL")
text = joke(url)


def text_to_speech():
    audio = gTTS(text=text, slow=True, lang="en")
    audio.save("video/audio.mp3")
