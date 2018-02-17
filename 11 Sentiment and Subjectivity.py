from textblob import TextBlob

# sentiment prediction
print(TextBlob("not a very great calculation").sentiment[0])
print(TextBlob("I had a great day.").sentiment[0])

# subjectivity and polarity
print("Subjectivity :: " + str(TextBlob("Hummus is Greek food").sentiment[1]))
print("Subjectivity :: " +str(TextBlob("Hummus is the most awesome dip to put on a pita").sentiment[1]))