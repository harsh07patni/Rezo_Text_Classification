__author__ = 'harsh'
import re
dictionary = {}
neg_words=""
pos_words=""
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
        #print row
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
        #wordcount is used for finding negation at back eg. not very good..
        wordcount = 4
        pos_words =""
        neg_words = ""
        for word in words:
            wordcount += 1
            for list_of_words, sentiment in dictionary.iteritems():
                if word.strip() == list_of_words.strip():
                    if sentiment == 'positive':
                        score += 1
                        pos_words = pos_words + word.strip() + ", "
                    elif sentiment == 'negative':
                        score -= 1
                        neg_words = neg_words + word.strip() + ", "

        print_sentiment(score)
