import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
THRESHOLD_FILE = PROJECT_ROOT / "config" / "thresholds.json"


def load_thresholds() -> dict:
    with open(THRESHOLD_FILE, encoding="utf-8") as file:
        return json.load(file)