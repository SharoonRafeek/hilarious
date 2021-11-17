from simple_image_download import simple_image_download as simp
import os
import shutil
response = simp.simple_image_download


def download_image(joke):
    if len(joke) > 50:
        joke = joke[:51]

    simple_images_dir = os.listdir("simple_images")

    if simple_images_dir != []:
        for dir in simple_images_dir:
            shutil.rmtree("simple_images/" + dir)

    response().download(joke, 1)

    image_dir = os.listdir("simple_images")[0]

    os.rename("simple_images/" + image_dir, "simple_images/image")
