import os
import string
from dotenv import load_dotenv
from joke_api.joke import joke
from audio.text_to_audio import text_to_speech
from image.image import download_image
from video.video import add_static_image_to_audio


load_dotenv()

url = os.getenv("JOKE_URL")
text = joke(url)

text_to_speech(text)
for char in string.punctuation:
    text = text.replace(char, '')

download_image(text)


audio_path = "assets/audio.mp3"
image_path = "dataset/image/" + os.listdir("dataset/image")[0]
output_path = "video/video.mp4"


add_static_image_to_audio(image_path, audio_path, output_path)
