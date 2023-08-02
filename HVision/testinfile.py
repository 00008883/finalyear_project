# import sqlite3
# # #
# # # # Initializing Database connection
# conn = sqlite3.connect('Data/detection.db')
# c = conn.cursor()
# c.execute("Select Count(*) from detections")
# print(c.fetchall())
#
# c.close()
# conn.close()
from SpeechRecognitionModule import SpeechRec
import speech_recognition as sr
from nltk.tokenize import sent_tokenize, word_tokenize

srm = SpeechRec()
try:
    text = srm.getUserSpeech(False)
    answer = srm.analyzeText(text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))


