import nltk

from nltk.corpus import wordnet as wn
from nltk import pos_tag
from nltk.tokenize import word_tokenize

def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']

def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']

def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']

def penn_to_wn(tag):
    if is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
    return None



stemmer = nltk.stem.WordNetLemmatizer()

s = "I would like to go for swimming as it is a good exercise."
tokens = word_tokenize(s)  # Generate list of tokens
tokens_pos = pos_tag(tokens)

singles = []
for touple in tokens_pos:
    pos = penn_to_wn(touple[1]);
    if pos:
        singles.append(stemmer.lemmatize(touple[0],pos))
    else:
        singles.append(stemmer.lemmatize(touple[0]))
print(' '.join(singles))
