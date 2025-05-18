# OpenAI-Based Voice Assistant with Memory

This script implements an AI-powered voice assistant using OpenAI's Assistants API v2 on a Raspberry Pi 5.

Features:
- Wake word detection ("Jarvis")
- Memory persistence across *sessions*
- Interaction with OpenAI's Assistant API
- Text-to-speech output (using a placeholder; requires a real-world TTS engine)

Dependencies:
- openai
- speech_recognition
- pyaudio (or a suitable alternative for audio input)
- subprocess (for text-to-speech on Raspberry Pi)
- os
- json
- datetime

Usage:
1. Set your OpenAI API key as an environment variable named `OPENAI_API_KEY`:
```shell
$ export OPENAI_API_KEY = your_api_key
```
2. Replace `YOUR_ASSISTANT_ID` with your assistant ID from OpenAI.
3. Install the required dependencies:

```shell
$ pip install openai speech_recognition pyaudio subprocess os json datetime
```
4. Install the Piper TTS Model:
   - Go to (link)[https://github.com/rhasspy/piper/blob/master/VOICES.md] and choose a voice that is fine for your lanuage, then download the model and replace the path in the code to the path where your model is at. Also make sure to specify the file too e.g
 ```shell
models/en_US-john-medium.omnx
```
5. Specify the memory file diirectory:
   - Create a file named memory.json or simmilar, then specify the directory to the file with the file included. This is where the conversation will be saved for memory and logs.
7. Run the script:
  ```shell
$ chmod +x main.py
$ python main.py
```
8. That's it!

## Bill of Materials
- Raspberry Pi 5
- 5/7" DSI/HDMI LCD
- Raspberry Pi Audio HAT
- NvMe HAT
- Speakers
- USB Mic
- NvMe SSD
- Raspberry Pi Cooler
- OpenAI and Picovoice credits (Or if you're using a different API then credits for those)
- Power Supply/PiSugar (Preferrably the PiSugar or UPS for portability)
- A case to fit all the hardware (Designed)
- Optional: Additional Hardware (Sensors, Relays, etc.) if you want a customized A.I
- Optional:
