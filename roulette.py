import random


class Roulette():
    def __init__(self, choice_list):
        self.choice_list = choice_list

    def roulette(self):
        choice_result = random.choice(self.choice_list)
        return choice_result
