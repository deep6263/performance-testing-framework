import os
import subprocess
import sys
from pathlib import Path
from utils.failure_rate_validator import validate_failure_rate
from utils.load_profile import get_profile
from utils.performance_threshold import validate_p95
from utils.threshold_loader import load_thresholds


PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOCUST_FILE = PROJECT_ROOT / "tests" / "locustfile.py"
REPORTS_DIR = PROJECT_ROOT / "reports"


def run_profile(profile_name: str) -> None:
    profile = get_profile(profile_name)
    thresholds = load_thresholds()
    report_dir = REPORTS_DIR / profile_name
    report_dir.mkdir(parents=True, exist_ok=True)

    env = os.environ.copy()
    env["LOAD_PROFILE"] = profile_name

    csv_prefix = report_dir / profile_name
    html_report = report_dir / f"{profile_name}_report.html"

    command = [
        "locust",
        "-f",
        str(LOCUST_FILE),
        "--headless",
        "-u",
        str(profile["users"]),
        "-r",
        str(profile["spawn_rate"]),
        "--run-time",
        profile["run_time"],
        "--csv",
        str(csv_prefix),
        "--html",
        str(html_report),
    ]

    print(f"Running performance profile: {profile_name}")
    print(f"Users: {profile['users']}")
    print(f"Spawn rate: {profile['spawn_rate']}")
    print(f"Run time: {profile['run_time']}")
    print(f"P95 threshold: {thresholds['p95_response_time_ms']} ms")
    print(f"Failure rate threshold: {thresholds['failure_rate_percent']}%")

    result = subprocess.run(command, env=env)

    if result.returncode != 0:
        print("Locust execution failed.")
        sys.exit(result.returncode)

    stats_file = Path(f"{csv_prefix}_stats.csv")

    try:
        validate_p95(
            stats_file,
            thresholds["p95_response_time_ms"],
        )
    except (AssertionError, ValueError) as error:
        print(f"Performance threshold validation failed: {error}")
        sys.exit(1)

    try:
        validate_failure_rate(
            stats_file,
            thresholds["failure_rate_percent"],
        )
    except (AssertionError, ValueError) as error:
        print(f"Failure rate validation failed: {error}")
        sys.exit(1)

    print("Performance threshold validation passed.")


if __name__ == "__main__":
    profile_name = os.getenv("LOAD_PROFILE", "smoke")
    run_profile(profile_name)
