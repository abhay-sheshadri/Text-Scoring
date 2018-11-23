import utils
import model
import dill
from xml.etree import ElementTree
from nltk.corpus import gutenberg

# Parses the xml file for training
def read_data(file):
    dataset = []
    tree = ElementTree.parse(file)
    root = tree.getroot()
    for doc in root:
        incorrect = []
        corrected = []
        offset = 0
        current_par = 0
        for p in doc[0]:
            incorrect.append(p.text)
            corrected.append(p.text)
        for m in doc[1]:
            if current_par != int(m.attrib["start_par"]):
                current_par = int(m.attrib["start_par"])
                offset=0
            s_char = int(m.attrib["start_off"])
            e_char = int(m.attrib["end_off"])
            correction = m[1].text
            corrected[current_par] = corrected[current_par][:s_char+offset] + correction + corrected[current_par][e_char+offset:]
            offset += len(correction) - (e_char - s_char)
        dataset += [("correct", sent) for p in corrected for sent in utils.get_set(p)]
        dataset += [("incorrect", sent) for p in incorrect for sent in utils.get_set(p)]
    return dataset

def main():
    dataset = read_data(r"training/data/official.xml")
    # To limit the chance that good grammar is classified as wrong, we add
    # some correct grammar from the gutenberg corpus to the dataset
    story = gutenberg.raw("burgess-busterbrown.txt")
    dataset += [("correct", sent) for sent in utils.get_set(story)]
    # Training
    rater = model.Model()
    rater.train(dataset)
    # Seriallize object
    with open(r"training/model.dill", 'wb') as save:
        dill.dump(rater, save)

if __name__ == '__main__':
    main()
