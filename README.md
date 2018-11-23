# Run
Open up a shell in the folder and enter: <br />
`python run.py` <br />
You can then enter sentences and recieve the scores.  Screenshots of examples are located in the screenshot folder.

# How it works
The model is trained on a dataset from the National University of Singapore as well as some stories by Thornton W. Burgess from the gutenberg corpus.
The model is fed a bunch of sentences that are grammatically correct and a bunch that are false.  It then tags the words by part of speech.
The frequency of trigrams of parts of speech tags in incorrect and correct sentences are counted.  When a sentence is scored, it is tagged and each trigram is labeled correct 
or incorrect depending on whether the trigram is more common in the  incorrect or correct sentences. The score is calculated using <br />
`score = number of correct trigrams in sentence / total number of trigrams in sentence * 10` <br />
The number is rounded.  
