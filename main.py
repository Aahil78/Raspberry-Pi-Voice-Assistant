import openai
import speech_recognition as sr
import pyaudio  # or a suitable alternative for audio input
import subprocess  # for potential text-to-speech on RPi
import os
import json
from datetime import datetime


# --- Configuration ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Set your OpenAI API key as an environment variable
ASSISTANT_ID = "YOUR_ASSISTANT_ID" # Replace with your assistant ID from OpenAI
WAKE_WORD = "jarvis"
MEMORY_FILE = "assistant_memory.json"

# --- Initialize OpenAI ---
openai.api_key = OPENAI_API_KEY


# --- Memory Management ---

def load_memory():
    try:
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_memory(messages):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(messages, f)


# --- Audio Input and Wake Word Detection ---
# (Placeholder – replace with a robust wake word detection library)

def detect_wake_word(audio_data):
    # In a real system, use a library like snowboy or porcupine
    # to detect the wake word accurately.
    text = transcribe_audio(audio_data)
    return WAKE_WORD in text.lower()


def transcribe_audio(audio_data):
    r = sr.Recognizer()
    try:
        text = r.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""


# --- OpenAI Assistant Interaction ---

def interact_with_assistant(user_message, messages):
    messages.append({"role": "user", "content": user_message})
    try:
      response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",  # or the appropriate Assistant model
          messages=messages,
          temperature=0.7
      )
      assistant_reply = response.choices[0].message.content
      messages.append({"role": "assistant", "content": assistant_reply})
      return assistant_reply
    except openai.error.OpenAIError as e:
      print(f"OpenAI API Error: {e}")
      return "I'm sorry, I encountered an error."


# --- Main Loop ---

if __name__ == "__main__":
    messages = load_memory()
    
    print(f"Assistant is ready. Wake word is '{WAKE_WORD}'.")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            audio = r.listen(source)
            if detect_wake_word(audio):
                print("Wake word detected!")
                user_input = transcribe_audio(audio) # Capture user speech after wake word
                if user_input:
                    print(f"User said: {user_input}")
                    response = interact_with_assistant(user_input, messages)
                    print(f"Assistant replied: {response}")
                    # Text-to-speech on Raspberry Pi
                    # subprocess.run(["espeak", response]) # Or other TTS engine
                    save_memory(messages)

