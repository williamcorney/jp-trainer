import random,json
class Theory():
    def __init__(self):
        self.load_data()

    def set_notes (self):

        return [60]

    def load_data(self):
        with open('theory.json', 'r') as file: self.Theory = json.load(file)