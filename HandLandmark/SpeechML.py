import nltk
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier
import pickle


def featureExtract(text):
    # Tokenizing the text using nltk
    words = nltk.tokenize.word_tokenize(text.lower())
    # Getting rid of unnecessary words and punctuations
    words = [word for word in words if word not in stopwords.words('english') and word.isalpha()]
    # Dictionary of features
    features = {}

    features["contains(yes)"] = "yes" in words
    features["contains(no)"] = "no" in words
    features["contains(do)"] = "do" in words
    features["contains(don't)"] = "don't" in words
    features["contains(feel)"] = "feel" in words
    features["contains(call)"] = "call" in words

    return features

train = [
    ("yes please", "agree"),
    ("no thanks", "not agree"),
    ("sure", "agree"),
    ("call ambulance", "agree"),
    ("don't call", "not agree"),
    ("feel okay", "not agree"),
    ("feel bad", "agree"),
    ("no way", "not agree"),
    ("okay call", "agree")
]

# Apply the feature extractor to each answer
train_set = [(featureExtract(text), label) for (text, label) in train]

# Train a model using nltk's NaiveBayesClassifier
classifier = nltk.NaiveBayesClassifier.train(train_set)

# Saving it in bytes using pickle
f = open("SpeechClassifier.pickle", "wb")
pickle.dump(classifier, f)
f.close()

