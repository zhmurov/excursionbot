"""Handler for the /start command."""
import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, Application

logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the command /start is issued."""
    user = update.effective_user
    logger.info(f"User {user.id} started the bot")
    
    welcome_message = (
        f"👋 Hi {user.first_name}!\n\n"
        "I'm your Location Facts Bot. I can tell you interesting facts about places near you!\n\n"
        "To get started:\n"
        "1. 📍 Share your location using Telegram's location sharing feature\n"
        "2. 🌟 I'll tell you an interesting fact about a nearby place\n\n"
        "You can also:\n"
        "• 🗺 Share your live location to get facts as you move around\n"
        "• 🔄 Send a new location anytime to learn about different places\n\n"
        "Ready to explore? Share your location and let's begin! 🚀"
    )
    
    await update.message.reply_text(welcome_message)

def register_start_handler(application: Application) -> None:
    """Register the start command handler."""
    application.add_handler(CommandHandler("start", start_command)) 