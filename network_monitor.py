"""Python Network Monitoring System.

Checks whether configured TCP endpoints accept connections, measures TCP
connection-establishment time, displays results, and logs them to CSV.
Run: python network_monitor.py
Stop: Ctrl+C
"""

import socket
import time
from datetime import datetime

from config import CSV_FILE, REFRESH_INTERVAL, TARGETS, TIMEOUT
from logger import save_result


def check_host(name: str, host: str, port: int, timeout: float = TIMEOUT):
    """Return (status, connection_time_ms, error_message).

    ONLINE means a TCP connection was established successfully. OFFLINE means
    the connection attempt failed; it does not prove the entire host is down.
    """
    started = time.perf_counter()

    try:
        with socket.create_connection((host, port), timeout=timeout):
            elapsed_ms = (time.perf_counter() - started) * 1000
        return "ONLINE", round(elapsed_ms, 2), ""
    except (OSError, ValueError) as exc:
        return "OFFLINE", None, str(exc)


def print_header() -> None:
    print("=" * 86)
    print("                         PYTHON NETWORK MONITOR")
    print("=" * 86)
    print(f"{'HOST':<22} {'IP / HOSTNAME':<22} {'PORT':<7} {'STATUS':<10} {'TCP TIME':<12} DETAILS")
    print("-" * 86)


def main() -> None:
    print_header()
    print(f"Refresh interval: {REFRESH_INTERVAL} seconds | Timeout: {TIMEOUT} seconds")
    print(f"CSV log: {CSV_FILE.resolve()}")
    print("Note: ONLINE means the selected TCP port accepted a connection.\n")

    try:
        while True:
            checked_at = datetime.now().astimezone().isoformat(timespec="seconds")
            print(f"\nChecked at: {checked_at}")
            print("-" * 86)

            for name, host, port in TARGETS:
                status, latency, error = check_host(name, host, port)
                latency_text = f"{latency:.2f} ms" if latency is not None else "N/A"
                details = "TCP connection succeeded" if status == "ONLINE" else error[:34]
                print(f"{name:<22} {host:<22} {port:<7} {status:<10} {latency_text:<12} {details}")

                try:
                    save_result(
                        timestamp=checked_at,
                        name=name,
                        host=host,
                        port=port,
                        status=status,
                        latency=latency,
                        details=error,
                    )
                except OSError as exc:
                    print(f"WARNING: Could not write CSV log: {exc}")

            print(f"\nNext check in {REFRESH_INTERVAL} seconds. Press Ctrl+C to stop.")
            time.sleep(REFRESH_INTERVAL)

    except KeyboardInterrupt:
        print("\nMonitoring stopped. Your saved CSV log has been preserved.")


if __name__ == "__main__":
    main()
