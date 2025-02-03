from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from src.constants import ENV_PATH

load_dotenv()


class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PASS: str
    DB_PORT: str
    DB_NAME: str

    DB_DRIVER: str

    DEBUG: bool = False

    def get_engine_link(self) -> str:
        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(extra="ignore")


def settings_factory() -> Settings:
    return Settings(_env_file=ENV_PATH)
