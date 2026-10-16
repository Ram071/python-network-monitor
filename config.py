"""Configuration for the Network Monitor."""

from pathlib import Path

# CSV is saved beside this project file, regardless of the terminal's directory.
PROJECT_DIR = Path(__file__).resolve().parent
CSV_FILE = PROJECT_DIR / "network_log.csv"

# How often to check all targets.
REFRESH_INTERVAL = 10

# Maximum time (seconds) to wait for each TCP connection attempt.
TIMEOUT = 3

# Format: (display name, host/IP address, TCP port)
TARGETS = [
    ("Google DNS", "8.8.8.8", 53),
    ("Cloudflare DNS", "1.1.1.1", 53),
    ("Local Computer", "127.0.0.1", 80),
]

# You can add your own server, for example:
# ("My Web Server", "192.168.1.10", 80),
