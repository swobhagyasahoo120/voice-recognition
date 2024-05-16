import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak out the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
            return ""
        except sr.RequestError as e:
            print(f"Request error from Google Speech Recognition service: {e}")
            return ""

# Function to greet user according to time
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

# Main function to interact with the user
def main():
    greet()
    speak("I am Jarvis. How may I assist you today?")
    while True:
        query = listen()
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
main()
