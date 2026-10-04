import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROFILE_FILE = PROJECT_ROOT / "config" / "load_profiles.json"


def load_profiles() -> dict:
    with open(PROFILE_FILE, encoding="utf-8") as file:
        return json.load(file)


def get_profile(name: str) -> dict:
    profiles = load_profiles()

    if name not in profiles:
        available_profiles = ", ".join(profiles.keys())
        raise ValueError(
            f"Unknown load profile '{name}'. "
            f"Available profiles: {available_profiles}"
        )

    return profiles[name]