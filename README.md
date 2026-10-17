# WhatsApp AI Chatbot

An automated WhatsApp Web chatbot that reads incoming chats, transcribes voice notes, and replies intelligently using the Groq API. It simulates human-like replies in Roman Urdu, acting as the user ("Rehan") in conversations.

---

## Features

- Automatically opens Chrome and navigates WhatsApp Web
- Reads the entire visible chat by dragging through the message history
- Detects and downloads voice notes, then transcribes them using **Whisper Large v3** (via Groq)
- Generates context-aware replies using **GPT-OSS-120B** (via Groq)
- Replies only when the other person has sent a message (skips your own messages)
- Fully automated using screen-based UI detection (no WhatsApp API required)

---

## Tech Stack

| Purpose | Library / Model |
|--------|-----------------|
| UI Automation | `pyautogui` |
| Clipboard access | `pyperclip` |
| AI replies | `groq` — `openai/gpt-oss-120b` |
| Voice transcription | `groq` — `whisper-large-v3` |
| Image detection | `opencv-python` (required by PyAutoGUI's `confidence` param) |

---

## Requirements

- Python 3.9+
- Google Chrome installed
- A free [Groq API key](https://console.groq.com/keys)
- WhatsApp Web already logged in on Chrome
- Screen resolution matched to the image templates (see *Note* below)

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/whatsapp-ai-chatbot.git
   cd whatsapp-ai-chatbot
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API key**
   - Copy `api_example.py` and rename the copy to `api.py`
   - Open `api.py` and replace `"YOUR_GROQ_API_KEY_HERE"` with your real key
   ```python
   groqapi = "gsk_xxxxxxxxxxxxxxxxxxxx"
   ```

5. **Log in to WhatsApp Web**
   - Open Chrome, go to [web.whatsapp.com](https://web.whatsapp.com), and scan the QR code.
   - Keep the chat window open with the conversation you want the bot to handle.

---

## Usage

Run the bot:

```bash
python main.py
```

- The bot will detect the Chrome icon and open it.
- It will read the current chat, respond to the latest message, and continue looping.
- A confirmation dialog appears every 2 cycles asking if you want to stop the program.

---

## Project Structure

```
whatsapp-ai-chatbot/
├── main.py              # Entry point — main loop & automation
├── ai_process.py        # Groq GPT reply generation
├── api_example.py       # Template for API key (copy → api.py)
├── api.py               # Your real API key (NOT uploaded to GitHub)
├── requirements.txt     # Python dependencies
├── .gitignore           # Files Git should ignore
├── *.jpg                # UI icon templates for PyAutoGUI
└── README.md
```

---

## Note on Image Templates

The bot relies on `.jpg` screenshots (`chrome_icon.jpg`, `voice_note_icon.jpg`, etc.) to detect UI elements on screen. If the bot fails to find them:

- Ensure your display scaling is set to **100%**
- Ensure Chrome is running at the same zoom level used when the screenshots were taken
- Replace the `.jpg` files with your own screenshots if needed

---

## Disclaimer

This project is for **educational purposes only**.

- Automating WhatsApp Web may violate [WhatsApp's Terms of Service](https://www.whatsapp.com/legal/terms-of-service) and could result in your account being restricted or banned.
- The bot controls your mouse and keyboard while running — do not touch the mouse or keyboard while it is active.
- Use at your own risk. The author is not responsible for any consequences (account bans, lost messages, etc.).

---

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).