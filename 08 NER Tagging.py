from nltk import word_tokenize, pos_tag, ne_chunk
text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'
print ne_chunk(pos_tag(word_tokenize(text)))
