from typing import Optional

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ConfigDataBase(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    DB_ECHO_LOG: bool = False

    @property
    def database_url(self) -> Optional[PostgresDsn]:
        logger.info(self.POSTGRES_USER)
        logger.info(self.POSTGRES_PASSWORD)
        logger.info(self.POSTGRES_HOST)
        logger.info(self.POSTGRES_PORT)
        logger.info(self.POSTGRES_DB)
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


settings_db = ConfigDataBase()
