from enum import Enum


class PostSourceType(str, Enum):
    URL = "url"
    MARKDOWN = "markdown"


class Platform(str, Enum):
    TELEGRAM = "telegram"
    DISCORD = "discord"
    MASTODON = "mastodon"
    MOCK_X = "mock_x"
    MOCK_LINKEDIN = "mock_linkedin"


class VariantStatus(str, Enum):
    DRAFT = "draft"
    APPROVED = "approved"
    REJECTED = "rejected"
    PUBLISHED = "published"


class PublishResultStatus(str, Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    RETRY = "retry"
