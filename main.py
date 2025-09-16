import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
import json
from google import genai
import os



recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "2f72262fbe9144259588de02c983841a"

def speak(text):
    engine.say(text)
    engine.runAndWait()

# pip install google-genai
# from google import genai

def aiProcess(command):
    # Initialize Gemini client
    client = genai.Client(api_key="AIzaSyBkHyn3XjLdxnp2fSptR7tmnoIhOUrnf24")

    # Combine system and user instruction into a single prompt
    prompt = f"""
You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud.
Give short responses please.

User: {command}
"""

    # Send the request to Gemini
    response = client.models.generate_content(
        model="gemini-2.0-flash",  # You can also try gemini-1.5-flash or gemini-1.5-pro
        contents=prompt
    )

    # Extract and return the generated text
    result = []
    for candidate in response.candidates:
        for part in candidate.content.parts:
            result.append(part.text)

    return " ".join(result)  # Join multiple parts into a single string


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://www.google.com")
        speak("Google is open now")
    elif "open youtube" in c.lower():
        webbrowser.open("http://www.youtube.com")
        speak("Youtube is open now")
    elif "open instagram" in c.lower():
        webbrowser.open("http://www.instagram.com")
        speak("Instagram is open now")
    elif "open whatsapp" in c.lower():
        webbrowser.open("http://www.whatsapp.com")
        speak("Whatsapp is open now")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "open spotify" in c.lower():
        os.startfile("Spotify.exe")
        speak("Spotify is open now")
    elif "news" in c.lower(): 
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
           data = r.json()  # Convert response to Python dictionary

        articles = data.get("articles", [])

        # print("\nTop Headlines:\n")
        for i, article in enumerate(articles, start=1):
          speak(f"{i}. {article['title']}")
    
    else:
        # lets openai handle the request
        output = aiProcess(c)
        speak(output)
        
  
 


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=5,phrase_time_limit=5)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes Vinay")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source,timeout=5,phrase_time_limit=5)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))



