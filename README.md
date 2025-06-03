# Location Facts Bot 🌍

A Telegram bot that provides interesting facts about locations shared by users. Simply send your location, and the bot will tell you an interesting fact about a nearby place!

## Features

- Get interesting facts about any location you share
- Support for both static locations and live location sharing
- Powered by GPT-4 for generating engaging and accurate facts
- Fast response times and reliable performance

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/locationbot.git
cd locationbot
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp env.example .env
```
Edit `.env` and add your:
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- OpenAI API Key (from [OpenAI Platform](https://platform.openai.com))

4. Run the bot:
```bash
python src/main.py
```

## Development

- Code formatting and linting is handled by Ruff
- Run `ruff check .` to check for issues
- Run `ruff format .` to format code

## Deployment

The bot is configured for deployment on Railway. See the [deployment documentation](docs/deployment.md) for details.

## License

MIT License - feel free to use this code for your own projects! 