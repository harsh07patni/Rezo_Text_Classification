__author__ = 'harsh'
import re
dictionary = {}
def readfile():
    lines=[]
    file = open("input.txt",'r')
    for line in file:
        lines.append(line)
    return lines

def initialize_dictionary():
    global dictionary
    reader = open("negative.txt",'r')
    for row in reader:
        dictionary[row.strip()]='negative'
    reader.close()
    reader = open("positive.txt",'r')
    for row in reader:
        dictionary[row.strip()] = 'positive'
    reader.close()


def print_sentiment(score):
    if(score>0):
        sentiment="positive"
    elif(score<0):
        sentiment="negative"
    else:
        sentiment="neutral"
    print(sentiment)


if __name__ == "__main__":
    lines = readfile()
    initialize_dictionary()
    for line in lines:
        score = 0
        words = re.sub(r'[^\w\s\d\']', '', line).split(" ")
        for word in words:
            for list_of_words, sentiment in dictionary.iteritems():
                if word.strip() == list_of_words.strip():
                    if sentiment == 'positive':
                        score += 1
                    elif sentiment == 'negative':
                        score -= 1
        print_sentiment(score)
