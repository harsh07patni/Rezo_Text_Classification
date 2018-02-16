from nltk.stem.porter import *

# Porter Stemmer
stemmer = PorterStemmer()

plurals = ['caresses', 'flies', 'dies', 'mules', 'denied',
            'died', 'agreed', 'owned', 'humbled', 'sized',
            'meeting', 'stating', 'siezing', 'itemization',
           'sensational', 'traditional', 'reference', 'colonizer',
           'plotted', 'generous']

singles = [stemmer.stem(plural) for plural in plurals]
print(' '.join(singles))

#SnowBall Stemmer
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
singles = [stemmer.stem(plural) for plural in plurals]
print(' '.join(singles))
