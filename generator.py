import random
import requests
import os


class WordGenerator:


    def __init__(self):
        self.url = "https://random-words5.p.rapidapi.com/getMultipleRandom"
        self.api_key = os.environ.get('API_KEY')
        self.api_headers = {'X-RapidAPI-Key': self.api_key,
                            'X-RapidAPI-Host': "random-words5.p.rapidapi.com"}
        self.params = {"count": "50"}
        self.words_list = None
        self.generate_vocab()

    def generate_vocab(self):
        response = requests.get(url=self.url, headers=self.api_headers, params=self.params)
        if response.status_code == requests.codes.ok:
            self.words_list = response.json()
        else:
            raise Exception("Word API is not getting responses.")

    def return_random_word(self):
        random_word = random.choice(self.words_list)
        return random_word
