
Python Network Monitoring System
A beginner-friendly Python project that tests configured TCP endpoints, measures
TCP connection-establishment time, prints a live terminal report, and saves
monitoring history to a CSV file.

Requirements
Python 3.9 or later recommended
Windows, macOS, or Linux
No third-party packages required
Project files
network_monitor.py — monitoring loop and TCP connection checks
config.py — target hosts, ports, timeout, refresh interval, CSV path
logger.py — CSV logging
requirements.txt — intentionally empty of external dependencies
network_log.csv — generated automatically at runtime
Run on Windows
Open Command Prompt or the VS Code terminal.

Change into this folder. Example:

cd Desktop\network_monitor
Check Python:

python --version
Start monitoring:

python network_monitor.py
Stop with Ctrl+C.

If python is not recognized on Windows, try:

py network_monitor.py
Customize targets
Edit TARGETS in config.py. Each entry has this format:

("Display Name", "hostname-or-IP", port_number)
Only monitor systems and services you are authorized to test.

Understanding the result
ONLINE: a TCP connection to the configured port succeeded.
OFFLINE: the connection attempt failed or timed out. This does not
necessarily mean the host is down; the port may be closed or a firewall may
block the connection.
TCP TIME: time to establish the TCP connection, not ICMP ping latency.
network_log.csv: one row per target per monitoring cycle.
DNS commonly uses UDP, but DNS also supports TCP. This program specifically
tests TCP port 53; it does not perform a DNS query.

Troubleshooting
If all public targets are offline, check your internet connection and firewall.
127.0.0.1:80 is offline unless a local service is listening on TCP port 80.
If CSV writing fails, check whether the folder is writable or the CSV is open
in another application.
The program waits for each target sequentially, so a slow/unreachable target
can delay the full cycle by up to the configured timeout.
Computer Networks concepts demonstrated
IP addressing, TCP connections, port numbers, connection timing, timeouts,
exception handling, repeated monitoring, and CSV-based logging.

⋮⋮⋮⋮⋮⋮⋮⋮
