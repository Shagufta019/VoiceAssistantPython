# Jarvis - AI Virtual Assistant

A full-featured AI virtual assistant built in Python. This assistant listens for your commands, speaks to you, controls your system, fetches live information from the internet, and uses advanced AI to chat naturally.

## Features

- **Wake Word Detection:** Responds when called by its wake word (e.g., "Jarvis").
- **Continuous Conversation & Memory:** After waking up, Jarvis enters a continuous listening loop allowing back-to-back commands and remembers the context of your conversation (remembers the last 10 messages).
- **App & Website Opener:** Opens requested websites (Google, YouTube, Facebook, GitHub, etc.) and local applications.
- **Music Player:** Plays curated music or videos from a pre-defined library.
- **News Updates:** Fetches and reads the latest top 5 news headlines from NewsAPI.
- **Live Weather Update:** Gets real-time weather information and conditions for any specified city using OpenWeatherMap.
- **AI Chat Mode:** For any general queries not covered by the defined commands, the assistant seamlessly routes the question to Groq's high-speed API running the powerful Llama model to get a smart, context-aware answer.

## Requirements

Before running the script, ensure you have installed the required libraries.

> **Note on Python Versions:**
> It is highly recommended to use Python 3.8 through 3.12. Using recent experimental versions (like Python 3.13 or 3.14) may cause the `pyaudio` package to fail during installation since pre-compiled wheels may not exist yet.

You can install all required dependencies easily using the provided text file:

```bash
pip install -r requirements.txt
```

*Note: For `pyaudio`, you may need specific tools on Windows depending on your Python version.*

## Setup & Configuration

1. **Credentials:** You need to configure your API keys in the `creds.py` file to enable all functionalities.
   - `newsapi`: Get your key from [NewsAPI](https://newsapi.org/)
   - `weatherapi`: Get your key from [OpenWeatherMap](https://openweathermap.org/)
   - `groqapi`: Get your key from [Groq](https://console.groq.com/)

   Create `creds.py` in the root folder with:
   ```python
   newsapi = "YOUR_NEWS_API_KEY"
   weatherapi = "YOUR_WEATHER_API_KEY"
   groqapi = "YOUR_GROQ_API_KEY"
   ```

2. **Custom Libraries:**
   - Add your music links to the `musicLibrary.py` dictionary.
   - Map your computer's applications to voice commands inside `apps.py`.

## Running the Assistant

Execute the main script:
```bash
python main.py
```

1. Wait for it to announce "Initializing...".
2. Say the wake word (e.g., "Jarvis") to activate the listening mode.
3. The assistant will reply "Yes". 
4. Give it your command. Since continuous conversation mode is enabled, it will wait for another command after completing the first one!
5. To end the conversation and send Jarvis back to sleep, say **"stop," "sleep," or "exit,"** or simply stay silent for 5 seconds.
