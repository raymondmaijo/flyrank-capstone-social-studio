from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "development"
    database_url: str = "sqlite:///./social_studio.db"
    redis_url: str = "redis://localhost:6379/0"
    telegram_bot_token: str = ""
    discord_bot_token: str = ""
    mastodon_access_token: str = ""
    social_adapter: str = "mock_x"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
