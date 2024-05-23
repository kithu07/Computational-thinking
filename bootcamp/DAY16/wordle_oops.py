SOURCE = "words.txt"

GREEN, YELLOW, RED = 'G', 'Y', 'R'
SPACE = ' '

import requests as rq
import json

class WordleSolver:
    wordlist = {}
    FIRST_TIME = True

    def __init__(self):
        if WordleSolver.FIRST_TIME:
            WordleSolver.FIRST_TIME = False
            WordleSolver.wordlist = [line.strip() for line in open(SOURCE)]
        self.words = WordleSolver.wordlist[:]
        load = json.dumps({"name"})
        reg = rq.post(REGISTER_URL, headers = JSON_HEADER, data = '{"name": "keerthana"}')
        if reg .status_code != HTTP_CREATED:
            raise RuntimeError(f'Something went wrong with registering')