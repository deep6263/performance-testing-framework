import json
import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"

load_dotenv(PROJECT_ROOT / ".env")


class Config:
    def __init__(self):
        self.environment = os.getenv("TEST_ENV", "qa")

        config_file = CONFIG_DIR / f"{self.environment}.json"

        if not config_file.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_file}"
            )

        with open(config_file, encoding="utf-8") as file:
            self.data = json.load(file)

    @property
    def base_url(self) -> str:
        return self.data["base_url"]

    @property
    def environment_name(self) -> str:
        return self.data["environment"]

config = Config()