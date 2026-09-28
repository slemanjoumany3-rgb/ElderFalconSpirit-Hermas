import os
import requests
from telegram_bot.bot import TelegramBot
from state.manager import StateManager

API_KEY = os.getenv("OPENCODE_ZEN_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALLOWED_USERS = os.getenv("TELEGRAM_ALLOWED_USERS")
STATE_KEY = os.getenv("STATE_ENCRYPTION_KEY")

def call_llm(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

def main():
    print("Hermes Agent is running...")
    state = StateManager(STATE_KEY)
    bot = TelegramBot(BOT_TOKEN, ALLOWED_USERS, call_llm, state)
    bot.run()

if __name__ == "__main__":
    main()
