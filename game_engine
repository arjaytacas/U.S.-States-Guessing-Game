import pandas

class GameEngine:
    def __init__(self):
        self.score = 0
        self.data = pandas.read_csv('50_states.csv')
        self.states = self.data.state.to_list()
        self.answered = []

    def scores(self):
        self.score +=1

    def add_to_list(self, input):
        self.answered.append(input)
