# -------------------------------
# VOICE ASSISTANT MINI PROJECT
# -------------------------------

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Function to make the assistant speak
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice input
def listen():
    with sr.Microphone() as source:
        print("\n🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduces background noise
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn’t understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, I’m having trouble connecting to the internet.")
            return ""

# Main program
def main():
    speak("Hello! I am your voice assistant. How can I help you today?")
    
    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! Nice to hear from you.")
        
        elif "time" in command:
            time_now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time_now}.")
        
        elif "date" in command:
            date_today = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today’s date is {date_today}.")
        
        elif "search" in command:
            query = command.replace("search", "").strip()
            if query:
                speak(f"Searching {query} on Google.")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                speak("Please say what you want me to search.")
        
        elif "stop" in command or "exit" in command or "goodbye" in command:
            speak("Goodbye! Have a nice day.")
            break
        
        elif command == "":
            continue  # Skip if no valid command recognized
        
        else:
            speak("Sorry, I can’t perform that task yet.")

# Run the assistant
if __name__ == "__main__":
    main()
