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
1. Set your OpenAI API key as an environment variable named `OPENAI_API_KEY`.
2. Replace `YOUR_ASSISTANT_ID` with your assistant ID from OpenAI.
3. Install the required dependencies:

```bash
$ pip install openai speech_recognition pyaudio
```
