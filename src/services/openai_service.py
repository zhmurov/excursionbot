"""Service for interacting with OpenAI API to generate location facts."""
import logging
from typing import Dict, Optional

from openai import AsyncOpenAI, APIError

from config import OPENAI_API_KEY, MAX_RETRIES, TIMEOUT

logger = logging.getLogger(__name__)

class OpenAIService:
    """Service for generating location facts using OpenAI."""

    def __init__(self) -> None:
        """Initialize the OpenAI client."""
        self.client = AsyncOpenAI(api_key=OPENAI_API_KEY, timeout=TIMEOUT)
        self._system_prompt = (
            "You are a knowledgeable local guide who provides interesting and accurate facts "
            "about locations. When given coordinates, you should:\n"
            "1. Identify a notable place, landmark, or area near those coordinates\n"
            "2. Share one interesting, specific fact about that place\n"
            "3. Keep responses concise (max 2-3 sentences)\n"
            "4. Focus on historical, cultural, or unique aspects\n"
            "5. Be accurate and factual, avoid speculation\n"
            "6. Don't mention the coordinates in the response"
        )

    async def generate_fact(self, latitude: float, longitude: float) -> str:
        """Generate an interesting fact about a location using GPT-4."""
        user_prompt = (
            f"Tell me an interesting fact about a notable place near these coordinates: "
            f"{latitude}, {longitude}. Remember to follow the guidelines in the system prompt."
        )

        for attempt in range(MAX_RETRIES):
            try:
                response = await self.client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {"role": "system", "content": self._system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.7,
                    max_tokens=150,
                    presence_penalty=0.6
                )
                return response.choices[0].message.content

            except APIError as e:
                logger.error(f"OpenAI API error on attempt {attempt + 1}: {str(e)}")
                if attempt == MAX_RETRIES - 1:
                    raise
                continue

            except Exception as e:
                logger.error(f"Unexpected error while generating fact: {str(e)}")
                raise

# Create a singleton instance
openai_service = OpenAIService() 