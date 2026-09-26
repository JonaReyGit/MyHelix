from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="MYHELIX_")

    cors_origins: list[str] = ["http://localhost:3000"]
    max_upload_bytes: int = 50 * 1024 * 1024


settings = Settings()
