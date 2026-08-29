from app.adapters.mock_linkedin_adapter import MockLinkedInPublisher
from app.adapters.mock_x_adapter import MockXPublisher
from app.adapters.telegram_adapter import TelegramPublisher

ADAPTERS = {
    "telegram": TelegramPublisher,
    "mock_x": MockXPublisher,
    "mock_linkedin": MockLinkedInPublisher,
}


def build_publisher(platform: str):
    cls = ADAPTERS[platform]
    return cls()
