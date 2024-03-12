from dotenv import load_dotenv

from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DB_ECHO: bool = True
    PROJECT_NAME: str = 'InterviewFy'
    VERSION: str = '1.0.0'
    DEBUG: bool = True
    CORS_ALLOWED_ORIGINS: str = 'http://localhost'


settings = Settings()
