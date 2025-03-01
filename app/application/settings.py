from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    ENV: str = Field("local", env="ENV")

    DATABASE_URL: Optional[str] = Field(None, env="DATABASE_URL")

    SECRET_KEY: str = Field(None, env="SECRET_KEY")
    ALGORITHM: str = Field(None, env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(None, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    class Config:
        env_file = ".env"

settings = Settings()
