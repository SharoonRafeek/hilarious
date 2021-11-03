from bing_image_downloader import downloader


def download_image(joke):
    downloader.download(joke, limit=1, verbose=False)
