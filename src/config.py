"""Configuration management for the Location Facts Bot."""
import os
from typing import Final

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Required environment variables
TELEGRAM_BOT_TOKEN: Final[str] = os.getenv("TELEGRAM_BOT_TOKEN", "")
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set")

OPENAI_API_KEY: Final[str] = os.getenv("OPENAI_API_KEY", "")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Optional environment variables with defaults
ENVIRONMENT: Final[str] = os.getenv("ENVIRONMENT", "development")
LOG_LEVEL: Final[str] = os.getenv("LOG_LEVEL", "INFO")

# Constants
FACT_GENERATION_INTERVAL: Final[int] = 600  # 10 minutes in seconds
MAX_RETRIES: Final[int] = 3  # Maximum number of retries for API calls
TIMEOUT: Final[int] = 30  # Timeout for API calls in seconds 