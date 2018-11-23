from nltk import trigrams
from collections import Counter, defaultdict
import utils

correct = 0
incorrect = 1

class Model(object):

    def __init__(self):
        # Will hold frequencies of trigrams in correct and incorrect sentences
        self.model = defaultdict(lambda: defaultdict(lambda: [0, 0]))

    def train(self, data):
        for sentence in data:
            # We increment correct if trigram in correct sentence
            if sentence[0] == "correct":
                for w1, w2, w3 in trigrams(sentence[1]):
                    self.model[(w1, w2)][w3][correct] +=1
            # We increment incorrect if trigram in incorrect sentence
            elif sentence[0] == "incorrect":
                for w1, w2, w3 in trigrams(sentence[1]):
                    self.model[(w1, w2)][w3][incorrect] +=1

    def rate(self, sentence):
        # Get parts of speech
        parts = utils.get_set(sentence)[0]
        # We count the number of incorrect trigrams vs total trigrams
        count = 0
        wrong = 0
        for w1, w2, w3 in trigrams(parts):
            count += 1
            if self.model[(w1, w2)][w3][incorrect] >= self.model[(w1, w2)][w3][correct]:
                wrong += 1
        # Percent of trigrams that are correct
        score = (count - wrong) / count
        return round(score * 10)
