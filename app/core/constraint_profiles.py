from dataclasses import dataclass


@dataclass(frozen=True)
class ConstraintProfile:
    platform: str
    max_chars: int
    tone: str
    max_hashtags: int
    allowed_emojis: bool = True


PROFILES = {
    "telegram": ConstraintProfile("telegram", 300, "friendly", 2, True),
    "discord": ConstraintProfile("discord", 500, "professional", 3, True),
    "mastodon": ConstraintProfile("mastodon", 450, "casual", 2, True),
    "mock_x": ConstraintProfile("mock_x", 280, "professional", 2, False),
    "mock_linkedin": ConstraintProfile("mock_linkedin", 700, "professional", 3, False),
}
