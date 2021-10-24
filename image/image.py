from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()


def download_image(joke):
    arguments = {"keywords": joke, "limit": 1,
                 "print_urls": False, "no_directory": "true", "format": "jpg", "output_directory": "image"}
    paths = response.download(arguments)
    print(paths)
