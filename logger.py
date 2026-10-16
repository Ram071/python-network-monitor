"""CSV logging helpers for the Network Monitor."""

import csv
from pathlib import Path
from typing import Optional, Union

from config import CSV_FILE

HEADERS = [
    "Timestamp",
    "Name",
    "Host",
    "Port",
    "Status",
    "Connection Time (ms)",
    "Error Details",
]


def save_result(
    timestamp: str,
    name: str,
    host: str,
    port: int,
    status: str,
    latency: Optional[float],
    details: str = "",
    csv_path: Union[str, Path] = CSV_FILE,
) -> None:
    """Append one result row and write a header when the CSV is new/empty."""
    path = Path(csv_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    needs_header = not path.exists() or path.stat().st_size == 0

    with path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if needs_header:
            writer.writerow(HEADERS)
        writer.writerow([
            timestamp,
            name,
            host,
            port,
            status,
            "" if latency is None else f"{latency:.2f}",
            details,
        ])
