# Hermes Agent

Hermes Agent is a lightweight Telegram bot powered by OpenCode Zen API.  
It runs entirely on GitHub Actions without any external server, VPS, or hosting.

## Features
- Telegram bot integration  
- OpenCode Zen API support  
- Persistent encrypted state  
- Auto-run every 6 hours  
- Fully serverless  
- Easy to deploy  

## Requirements
You must add the following secrets in your GitHub repository:

- `OPENCODE_ZEN_API_KEY`
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_ALLOWED_USERS`
- `STATE_ENCRYPTION_KEY`

## Installation
1. Upload all project files to your GitHub repository  
2. Add the required secrets  
3. Go to **Actions** → Run the workflow  
4. Your Telegram bot will start responding immediately  

## Notes
- The bot only responds to allowed Telegram user IDs  
- State is encrypted using `STATE_ENCRYPTION_KEY`  
- The workflow runs automatically every 6 hours  

## License
MIT License
