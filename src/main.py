"""Entry point for the Location Facts Bot."""
import asyncio
import logging
from typing import NoReturn

from telegram.ext import ApplicationBuilder, Application

from config import TELEGRAM_BOT_TOKEN, LOG_LEVEL
from handlers.start_handler import register_start_handler
from handlers.location_handler import register_location_handler
from utils.logger import setup_logging

logger = logging.getLogger(__name__)

async def main() -> NoReturn:
    """Initialize and run the bot."""
    # Setup logging
    setup_logging()
    logger.info("Starting Location Facts Bot...")

    # Create the Application and pass it your bot's token
    application = (
        ApplicationBuilder()
        .token(TELEGRAM_BOT_TOKEN)
        .build()
    )

    # Register handlers
    register_start_handler(application)
    register_location_handler(application)

    # Start the bot
    logger.info("Bot is ready to serve facts!")
    await application.run_polling(allowed_updates=["message", "edited_message"])

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Bot stopped due to error: {e}", exc_info=True) 