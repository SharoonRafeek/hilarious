import os
from dotenv import load_dotenv
from joke_api.joke import joke
from audio.text_to_audio import text_to_speech
from image.image import download_image
from video.video import add_static_image_to_audio


load_dotenv()

url = os.getenv("JOKE_URL")
text = joke(url)

# text_to_speech(text)
new_text = ""
for char in text:
    if char != ",":
        new_text += char


# download_image(new_text)

audio_path = "assets/audio.mp3"
image_path = "assets/1.made-a-graph-of-my-past-relationships-i-have-an-58467322.png"
output_path = "video/video.mp4"

add_static_image_to_audio(image_path, audio_path, output_path)
