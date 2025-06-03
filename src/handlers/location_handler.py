"""Handler for location messages and live location updates."""
import logging
from datetime import datetime, timedelta
from typing import Dict, Optional

from telegram import Update, Location
from telegram.ext import (
    ContextTypes,
    MessageHandler,
    filters,
    Application,
)

from config import FACT_GENERATION_INTERVAL
from services.openai_service import openai_service

logger = logging.getLogger(__name__)

# Store last fact generation time for live location users
last_fact_time: Dict[int, datetime] = {}

async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle received location updates."""
    if not update.message or not update.message.location:
        return

    user = update.effective_user
    location: Location = update.message.location
    user_id: int = user.id

    logger.info(
        f"Received location from user {user_id}: "
        f"lat={location.latitude}, lon={location.longitude}, live={location.live_period is not None}"
    )

    # Handle live location
    if location.live_period:
        current_time = datetime.now()
        last_time = last_fact_time.get(user_id)

        # Generate fact if it's the first live location or enough time has passed
        if not last_time or (current_time - last_time) >= timedelta(seconds=FACT_GENERATION_INTERVAL):
            last_fact_time[user_id] = current_time
            await generate_and_send_fact(update, location)
        return

    # Handle regular location
    await generate_and_send_fact(update, location)

async def generate_and_send_fact(update: Update, location: Location) -> None:
    """Generate and send a fact about the given location."""
    user = update.effective_user
    try:
        # Show typing indicator while generating fact
        async with update.message.chat.action("typing"):
            fact = await openai_service.generate_fact(location.latitude, location.longitude)
        
        await update.message.reply_text(
            f"🌟 {fact}\n\n"
            "Send another location to learn more interesting facts! 🗺"
        )
        logger.info(f"Sent fact to user {user.id}")

    except Exception as e:
        error_message = (
            "Sorry, I couldn't generate a fact about this location right now. "
            "Please try again in a moment! 🙏"
        )
        await update.message.reply_text(error_message)
        logger.error(f"Error generating fact for user {user.id}: {str(e)}")

def register_location_handler(application: Application) -> None:
    """Register the location message handler."""
    application.add_handler(
        MessageHandler(
            filters.LOCATION | filters.StatusUpdate.LOCATION,
            handle_location
        )
    ) 