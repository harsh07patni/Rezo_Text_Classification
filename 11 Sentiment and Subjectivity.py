from textblob import TextBlob

# sentiment prediction
print(TextBlob("not a very great calculation").sentiment)

# subjectivity and polarity (openion mining)
print("Subjectivity :: " + str(TextBlob("Hummus is Greek food").sentiment[1]))
print("Subjectivity :: " +str(TextBlob("Hummus is the most awesome dip to put on a pita").sentiment[1]))