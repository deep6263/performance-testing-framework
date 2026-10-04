from pathlib import Path
import csv


def validate_p95(report_file: Path, max_p95_ms: float) -> None:
    with open(report_file, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row.get("Name") == "Aggregated":
                p95 = float(row["95%"])

                if p95 > max_p95_ms:
                    raise AssertionError(
                        f"P95 response time {p95:.0f} ms "
                        f"exceeded the threshold of {max_p95_ms:.0f} ms"
                    )

                print(
                    f"P95 response time {p95:.0f} ms "
                    f"is within the threshold of {max_p95_ms:.0f} ms"
                )
                return

    raise ValueError("Aggregated performance result not found.")