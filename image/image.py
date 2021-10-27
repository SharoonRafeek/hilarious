from PIL import Image
import os
from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()


def download_image(joke):
    assets = os.listdir("assets")
    for asset in assets:
        if asset[-4:] == ".png":
            os.remove(f"assets/{asset}")
            break

    arguments = {"keywords": joke, "limit": 1,
                 "print_urls": False, "no_directory": "true", "format": "png", "output_directory": "assets"}
    response.download(arguments)

    assets = os.listdir("assets")
    for asset in assets:
        if asset[-4:] == ".png":
            os.rename(f"assets/{asset}", "assets/image.png")

    current_directory = os.getcwd()
    image_directory = current_directory + "/assets/image.png"

    image = Image.open(image_directory)
