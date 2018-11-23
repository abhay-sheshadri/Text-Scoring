import nltk
from collections import Counter, defaultdict

# Tokenize text into a list of lists of words
def text_to_word_sets(text):
    sets = []
    for sentence in nltk.tokenize.sent_tokenize(text):
        sets.append(nltk.tokenize.word_tokenize(sentence))
    return sets

# Prepares words
def edit_set(text):
    sets = text_to_word_sets(text)
    for i in range(len(sets)):
        sets[i] = nltk.pos_tag(sets[i])
        sets[i] = nltk.ne_chunk(sets[i])
    return sets

# Given text will return lists of sentences as parts of speech
def get_set(text):
    uncleaned_sets = edit_set(text)
    cleaned_sets = []
    for i in range(len(uncleaned_sets)):
        cleaned_sets.append([])
        for sub in uncleaned_sets[i]:
            if type(sub) is nltk.Tree:
                cleaned_sets[i].append("{0}-{1}".format(sub.label(),
                                                        sub[0][1]))
            else:
                cleaned_sets[i].append(sub[1])
    return cleaned_sets
