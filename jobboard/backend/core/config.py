import os
from pathlib import Path
from dotenv import dotenv_values
env_path = Path(".")/'.env'
config = dotenv_values(env_path)


class Settings:

    PROJECT_TITLE: str = "Jobboard"
    PROJECT_VERSION: str = "0.1.1"
    POSTGRES_USER: str = config.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = config.get("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = config.get("POSTGRES_SERVER")
    POSTGRES_PORT: str = config.get("POSTGRES_PORT")
    POSTGRES_DB: str = config.get("POSTGRES_DB")
    DATABASE_URL: str = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'


settings = Settings()
