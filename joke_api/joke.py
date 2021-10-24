import requests
import json


def joke(url):
    response = requests.get(url)
    data = response.json()
    if data["type"] == "twopart":
        joke = f'''{data['setup']} {data['delivery']}'''
    elif data["type"] == "single":
        joke = data["joke"]

    return joke
