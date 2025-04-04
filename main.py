import os
import json
import pvporcupine
import sounddevice as sd
import numpy as np
import openai
import piper.tts

# OpenAI API Key
openai.api_key = "your_openai_api_key"

# Memory File
MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_response(prompt, memory):
    context = "\n".join(memory.get("history", [])) + f"\nUser: {prompt}\nAI:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": context}]
    )
    return response["choices"][0]["message"]["content"]

def synthesize_speech(text):
    tts = piper.tts.Piper(model_path="path_to_piper_model")
    tts.synthesize(text)

def detect_wakeword():
    porcupine = pvporcupine.create(keyword_paths=["path_to_jarvis.ppn"])
    stream = sd.InputStream(channels=1, samplerate=porcupine.sample_rate, callback=lambda indata, frames, time, status: porcupine.process(indata.flatten()))
    stream.start()
    while True:
        if porcupine.process(np.zeros(porcupine.frame_length)) >= 0:
            return True

def main():
    memory = load_memory()
    print("Listening for 'Jarvis' wake word...")
    
    while True:
        if detect_wakeword():
            user_input = input("You: ")  # Replace with actual speech-to-text processing
            response = get_response(user_input, memory)
            print(f"AI: {response}")
            synthesize_speech(response)
            
            memory.setdefault("history", []).append(f"User: {user_input}")
            memory["history"].append(f"AI: {response}")
            save_memory(memory)

if __name__ == "__main__":
    main()
