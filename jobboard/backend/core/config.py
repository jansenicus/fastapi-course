import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'

class settings:
    PROJECT_TITLE: str = "Jobboard"
    PROJECT_VERSION: str = "0.1.1"


settings = Settings()
