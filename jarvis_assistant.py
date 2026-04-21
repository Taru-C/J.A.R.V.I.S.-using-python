import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)  # Control speaking speed

def speak(audio):
    """Make Jarvis speak"""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Greet the user based on the time"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning! How may I help you today?")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening! How was your day Luna?")
    speak("How may I help you?")

def takeCommand(): 
    """Takes microphone input and returns recognized speech"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    speak("Hey, I am your personal assistant Jarvis.")
    wishMe()

    running = True  # To control the main loop

    while running:
        print("Say 'Hey Jarvis' or 'Hey Buddy' to wake me up...")
        wake_word = takeCommand().lower()

        if "jarvis" in wake_word or "hey buddy" in wake_word:
            speak("Yes Luna, I’m listening...")
            print("Activated!")

            query = takeCommand().lower()

            # -------- Main Commands --------
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak("Opening YouTube")
                webbrowser.open("https://youtube.com")

            elif 'open google' in query:
                speak("Opening Google")
                webbrowser.open("https://google.com")

            elif 'play music' in query:
                speak("Playing music on YouTube Music")
                webbrowser.open("https://music.youtube.com/")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Luna, the time is {strTime}")

            elif 'open code' in query:
                speak("Opening Visual Studio Code")
                codePath = "C:\\Users\\echoe\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'open whatsapp' in query:
                speak("Opening WhatsApp Web")
                webbrowser.open("https://web.whatsapp.com/")

            elif 'play a movie' in query:
                speak("Opening Disney Plus Hotstar")
                webbrowser.open("https://www.disneyplus.com/en-in/movies")

            elif 'who are you' in query:
                speak("I am Jarvis, your personal AI assistant. I am here to make your life easier and more organized.")

            elif 'how are you' in query:
                speak("I am fine, thank you for asking Luna. How can I assist you today?")

            elif 'thank you' in query:
                speak("You're welcome Luna. Always here to help you.")

            elif 'what can you do' in query:
                speak("I can help you with many tasks like searching Wikipedia, opening websites, playing music, telling the time, and much more. Just ask me what you need.")

            elif 'stop' in query or 'exit' in query or 'sleep' in query:
                speak("Okay Luna, going to sleep. Have a great day!")
                running = False  # Properly stop the loop
                break

            else:
                speak("Sorry Luna, I didn’t understand that. Can you say it again?")

elif 'take note' in query:
    speak("What should I write?")
    note = takeCommand()
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    speak("Note saved")
