import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import client
import apps
import os
import creds

r = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    # Opens any website by using Windows search based on the user's voice command
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")

    # Opens any app or website by using Windows search based on the user's voice command
    elif c.lower().startswith("open"):
        app = c.lower().replace("open", "").strip()

        # Check if the app is in our predefined dictionary
        command = apps.apps.get(app)

        if command:
            if command.startswith("start "):
                full_command = command
            else:
                full_command = f'start "" "{command}"'
        else:
            full_command = f'start "" "{app}"'

        exit_code = os.system(full_command)
        
        if exit_code == 0:
            speak(f"Opening {app}")
        else:
            speak(f"Sorry, I could not open {app}")

    # Plays a song by extracting its name from the command and opening the corresponding link from the music library
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/everything?q=india&language=en&sortBy=publishedAt&apiKey={creds.newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles and limit to the top 5
            articles = data.get("articles", [])[:5]

            # Say the headline
            for article in articles:
                speak(article["title"])

    elif "weather" in c.lower():
        if "in" in c.lower():
            city = c.lower().split("in")[-1].strip()
        else:
            city = "Bokaro Steel City"   # default city


        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={creds.weatherapi}&units=metric")
        data = r.json()

        if "main" in data:
            temp = data["main"]["temp"]
            feels = data["main"]["feels_like"]
            desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            speak(f"In {city}, it's {temp}°C, feels like {feels}°C with {desc}. Humidity is {humidity} percent.")
        else:
            print(data) #debug
            speak("Sorry, I couldn't fetch the weather")
    else:
        # If the command doesn't match any specific tasks, ask Groq
        output = client.aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    
    while True:
        r = sr.Recognizer()
        try:
            # Obtain audio from microphone
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
            # Recognize speech using Google
            print("Recognizing...")
            word = r.recognize_google(audio)

            if("jarvis" in word.lower()):
                speak("Yes")
                
                # Continuous conversation loop
                while True:
                    try:
                        with sr.Microphone() as source:
                            print("Jarvis Active... (listening for next command)")
                            # Increased the time limits to allow longer commands
                            audio = r.listen(source, timeout=5, phrase_time_limit=10)
                            
                        command = r.recognize_google(audio)
                        
                        # Command to manually exit active conversation mode
                        if "sleep" in command.lower() or "stop" in command.lower() or "exit" in command.lower():
                            speak("Okay.")
                            break
                        
                        processCommand(command)
                        
                    except Exception as e:
                        # If silence or unrecognizable speech occurs, break the loop
                        # This returns it to the main wake word loop
                        print("Returning to wake-word detection mode...")
                        break

        except Exception as e:
            print(f"Error: {e}")
