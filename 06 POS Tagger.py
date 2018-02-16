from nltk import pos_tag
from nltk.tokenize import word_tokenize

s = "This is a simple sentence. I would like to go for swimming."
tokens = word_tokenize(s)  # Generate list of tokens
tokens_pos = pos_tag(tokens)
print(tokens_pos)

