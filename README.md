# WhatsApp AI Chatbot

An automated WhatsApp Web chatbot that reads messages, transcribes voice notes, and generates natural Roman Urdu replies using Groq AI as Rehan.

## Features
- Automates Chrome and WhatsApp Web using PyAutoGUI.
- Reads chat history and detects incoming messages.
- Transcribes voice notes using Whisper Large v3.
- Generates context-aware replies using GPT-OSS-120B.
- Skips your own messages and automates replies.

## Tech Stack
- Python, PyAutoGUI, Pyperclip
- Groq API, Whisper Large v3, GPT-OSS-120B
- OpenCV

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/rehan-ahmad10/whatsapp-ai-chatbot.git
   cd whatsapp-ai-chatbot
   ```
2. Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create `api.py` from `api_example.py` and add your Groq API key.
5. Log in to WhatsApp Web using Chrome.

## Usage
Run the chatbot:
```bash
python main.py
```

Keep the target chat open while the bot runs.

## Note
Screen automation depends on display scaling and image templates. Use responsibly, as automation may violate WhatsApp's Terms of Service.

## License
MIT License