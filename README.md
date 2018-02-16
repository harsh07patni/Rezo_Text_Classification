# Rezo.AI - Text Classification Basics Using Python 2.x

The tutorials are for people attending UpGrad workshop happening on 18th Feb 2018. The course is created for beginners who want to explore text analytics .

## Getting Started

You should have basic knowledge about python before you begin this course.

## Prerequisites

* [Python 2.7](https://www.python.org/downloads/) - Language
* [Pycharm](https://www.jetbrains.com/pycharm/download/) - IDE
* [NLTK](http://www.nltk.org/install.html) - Natural Language Python Package
* [PIP] - it should be already there if you have installed python 2.7


### Installing NLTK Packages

Once Pycharm is configured with python and  NLTK is installed in your system. Please download the following as well using the below syntex in a python file using pycharm.

```
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')
nltk.download('wordnet')

```

### Install TextBlob

```
pip install -U textblob
python -m textblob.download_corpora

```

For language detection code internet connectivity will be required. Though it's ok if you dont have it. It's not a compulsion# Rezo_Text_Classification
