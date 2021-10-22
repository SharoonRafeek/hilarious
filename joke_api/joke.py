import requests
import json


def joke(url):
    response = requests.get(url)
    data = response.json()
    joke = data['setup'] + " " + data['delivery']

    return joke
