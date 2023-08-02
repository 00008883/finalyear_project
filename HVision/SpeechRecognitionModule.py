import speech_recognition as sr
import nltk
import pickle
import SpeechML
from nltk.corpus import stopwords


class SpeechRec:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        # Setting microphone as an input device
        with sr.Microphone() as source:
            print("Speak:")
            self.audio = self.recognizer.listen(source)

    def getUserSpeech(self, offline_mode = True):
        # Offline or Online mode
        self.offline_mode = offline_mode
        if self.offline_mode:
            # Speech recognition using OpenAI whisper
            self.voice_input = self.recognizer.recognize_whisper(self.audio, language="english", model="small")
            print("You said: " + self.voice_input)
            return self.voice_input
        else:
            # Speech recognition using Google Default API key
            self.voice_input = self.recognizer.recognize_google(self.audio)
            print("You said: " + self.voice_input)
            return self.voice_input


    # def preprocessText(self, text):
    #     user_text = text
    #     sentences = nltk.tokenize.sent_tokenize(user_text.lower())
    #     tokens = [nltk.tokenize.word_tokenize(sent) for sent in sentences]
    #     filteredText = [token for token in tokens if token not in stopwords.words('english')]
    #     # self.lemmatizer = nltk.stem.WordNetLemmatizer()
    #     # self.lemmatizedText = [self.lemmatizer.lemmatize(token) for token in self.filteredText]
    #     print(filteredText)

    def analyzeText(self, text):
        # Loading classifier from already created pickle file
        f = open("SpeechClassifier.pickle", "rb")
        classifier = pickle.load(f)
        f.close()

        # Classifying data using SpeechML module
        token_set = [SpeechML.featureExtract(text)]
        resultList = classifier.classify_many(token_set)
        result = resultList[0]
        print(result)
        return result
