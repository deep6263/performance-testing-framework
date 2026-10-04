import csv
from pathlib import Path


def validate_failure_rate(
    report_file: Path,
    max_failure_rate: float,
) -> None:
    with open(report_file, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row.get("Name") == "Aggregated":
                requests = int(row["Request Count"])
                failures = int(row["Failure Count"])

                if requests == 0:
                    raise ValueError("No requests were recorded.")

                failure_rate = (failures / requests) * 100

                if failure_rate > max_failure_rate:
                    raise AssertionError(
                        f"Failure rate {failure_rate:.2f}% "
                        f"exceeded the threshold of "
                        f"{max_failure_rate:.2f}%"
                    )

                print(
                    f"Failure rate {failure_rate:.2f}% "
                    f"is within the threshold of "
                    f"{max_failure_rate:.2f}%"
                )
                return

    raise ValueError("Aggregated performance result not found.")