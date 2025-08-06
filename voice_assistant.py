import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import webbrowser  


listener = sr.Recognizer()
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  

def talk(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("You:", command)
            return command
    except:
        talk("Sorry, I didn't catch that.")
        return ""

def play_on_youtube(query):
    """Plays video directly using pywhatkit or opens browser"""
    try:
        talk(f"Playing {query} on YouTube")
        pywhatkit.playonyt(query)  
    except Exception as e:
        print("Error:", e)
        talk("Opening in browser instead")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def run_assistant():
    talk("Hi, I am your voice assistant. How can I help you?")

    while True:
        command = listen()

        if 'hello' in command:
            talk("Hello! How can I assist you today?")

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The current time is {time}")

        elif 'date' in command:
            date = datetime.datetime.now().strftime('%A, %B %d, %Y')
            talk(f"Today is {date}")

        elif 'play' in command:
            song = command.replace('play', '').strip()
            if song:
                play_on_youtube(song)
            else:
                talk("Please tell me what to play")

        elif 'search' in command:
            topic = command.replace('search', '').strip()
            talk(f"Searching for {topic}")
            pywhatkit.search(topic)

        elif 'exit' in command or 'bye' in command:
            talk("Goodbye! Have a nice day.")
            break

        elif command:
            talk("Sorry, I didn't understand. Please try again.")

# Run the assistant
run_assistant()