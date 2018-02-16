import textblob as tb
from textblob import classifiers

training = [
('Tom Holland is a terrible spiderman.','pos'),
('a terrible Javert (Russell Crowe) ruined Les Miserables for me...','pos'),
('The Dark Knight Rises is the greatest superhero movie ever!','neg'),
('Fantastic Four should have never been made.','pos'),
('Wes Anderson is my favorite director!','neg'),
('Captain America 2 is pretty awesome.','neg'),
('Lets pretend "Batman and Robin" never happened..','pos'),
]
testing = [
('Superman was never an interesting character.','neg'),
('Fantastic Mr Fox is an awesome film!','pos'),
('Dragonball Evolution is simply terrible!!','neg')
]

classifier = classifiers.NaiveBayesClassifier(training)
print ("Error Rate :: " + str(classifier.accuracy(testing)))
classifier.show_informative_features(3)


blob = tb.TextBlob('the weather is terrible!', classifier=classifier)
print ("Prediction :: " + blob.classify())