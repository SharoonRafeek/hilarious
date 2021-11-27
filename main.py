import os
import string
import time
from dotenv import load_dotenv
from joke_api.joke import joke
from audio.text_to_audio import text_to_speech
from image.image import download_image
from video.video import add_static_image_to_audio
from video.upload_video import upload_video


load_dotenv()
url = os.getenv("JOKE_URL")


def main():
    while True:

        def collecting_image_audio():
            text = joke(url)
            title = text
            text_to_speech(text)
            for char in string.punctuation:
                text = text.replace(char, '')

            download_image(text)

            image = os.listdir("simple_images/image")

            if len(image) == 0:
                collecting_image_audio()
            else:
                return image, title

        image, title = collecting_image_audio()

        audio_path = "assets/audio.mp3"
        image_path = "simple_images/image/" + image[0]
        output_path = "video/video.mp4"

        add_static_image_to_audio(image_path, audio_path, output_path)

        client_id = os.getenv("CLIENT_ID")
        client_secret = os.getenv("CLIENT_SECRET")
        access_token = os.getenv("ACCESS_TOKEN")
        refresh_token = os.getenv("REFRESH_TOKEN")

        upload_video(client_id, client_secret, access_token, refresh_token, title)

        time.sleep(10800)


if __name__ == "__main__":
    main()
