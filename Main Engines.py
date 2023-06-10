import speech_recognition as sr
import pyttsx3
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

engine = pyttsx3.init()
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: ", text)
        return text
    except:
        print("Sorry, could not recognize your voice.")
        return ""

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(text)['compound']
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"

def aleena():
    print("Hi! I'm Aleena, your personal assistant.")
    speak("Hi! I'm Aleena, your personal assistant.")
    while True:
        text = listen().lower()
        if "stop" in text:
            speak("Goodbye!")
            break
        else:
            sentiment = analyze_sentiment(text)
            if sentiment == "positive":
                speak("I'm glad to hear that.")
            elif sentiment == "negative":
                speak("I'm sorry to hear that.")
            else:
                speak("I'm not sure what you mean.")
            speak("Is there anything else I can help you with?")
aleena()