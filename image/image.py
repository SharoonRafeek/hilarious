from bing_image_downloader import downloader
import os
import shutil


def download_image(joke):
    dataset_dir = os.listdir("dataset")

    if dataset_dir != []:
        for dir in dataset_dir:
            shutil.rmtree("dataset/" + dir)

    downloader.download(joke, adult_filter_off=True, limit=1)

    image_dir = os.listdir("dataset")[0]

    os.rename("dataset/" + image_dir, "dataset/image")
