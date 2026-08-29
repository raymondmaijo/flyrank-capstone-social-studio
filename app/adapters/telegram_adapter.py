import httpx

from app.adapters.base import SocialPublisher
from app.config import settings


class TelegramPublisher(SocialPublisher):
    platform = "telegram"

    def publish(self, *, variant_id: str, content: str, metadata: dict) -> dict:
        url = f"https://api.telegram.org/bot{settings.telegram_bot_token}/sendMessage"
        payload = {"chat_id": metadata.get("chat_id", "demo-chat"), "text": content}
        response = httpx.post(url, json=payload, timeout=15)
        response.raise_for_status()
        result = response.json()
        return {
            "platform": "telegram",
            "success": True,
            "post_url": f"https://t.me/{metadata.get('chat_id', 'demo-chat')}",
            "external_id": result.get("result", {}).get("message_id"),
        }
