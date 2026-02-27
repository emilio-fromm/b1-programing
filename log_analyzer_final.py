# Copyright by Emilio

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

LOG_FILE = "example_log.txt"

failed_logins = {}
security_incidents = []
error_entries = []
ip_request_count = {}

print("Starting log analysis...")

try:
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    logging.error(f"Log file '{LOG_FILE}' not found")
    lines = []
except PermissionError:
    logging.error(f"No permission to read '{LOG_FILE}'")
    lines = []

print("deubg - lines loaded:", len(lines))

for line in lines:
    line = line.strip()
    if not line:
        continue

    try:
        parts = line.split(" ")
        ip = parts[0]
        ip_request_count[ip] = ip_request_count.get(ip, 0) + 1

        status_code = None
        for part in parts:
            if part.isdigit() and len(part) == 3:
                status_code = int(part)
                break

        if status_code is None:
            continue

        is_login = "/login" in line

        if status_code == 401 and is_login:
            if ip not in failed_logins:
                failed_logins[ip] = 0
            failed_logins[ip] = failed_logins[ip] + 1

            if failed_logins[ip] >= 3:
                incident = f"Brute-Force from {ip} - {failed_logins[ip]} failed attempts"
                if incident not in security_incidents:
                    security_incidents.append(incident)
                    logging.warning(incident)

        if status_code == 403:
            incident = f"Forbidden access: {ip} -> {line}"
            security_incidents.append(incident)
            logging.warning(f"403 Forbidden from {ip}")

        suspicious_agents = ["sqlmap", "nikto", "nmap", "masscan"]
        for agent in suspicious_agents:
            if agent in line.lower():
                incident = f"Suspicious tool detected ({agent}) from {ip}"
                security_incidents.append(incident)
                logging.warning(incident)

        if status_code >= 400:
            error_entries.append(f"[{status_code}] {line}")

    except Exception as e:
        logging.error(f"Line could not be parsed: {e}")
        continue

try:
    with open("security_incidents.txt", "w") as f:
        f.write("=== SECURITY INCIDENTS ===\n\n")
        f.write(f"Total incidents: {len(security_incidents)}\n\n")

        f.write("--- Brute-Force Attempts ---\n")
        for ip, count in failed_logins.items():
            if count >= 3:
                f.write(f"{ip}: {count} failed attempts\n")

        f.write("\n--- All Incidents ---\n")
        for incident in security_incidents:
            f.write(incident + "\n")

        f.write("\n--- Top IPs by Request Count ---\n")
        sorted_ips = sorted(ip_request_count.items(), key=lambda x: x[1], reverse=True)
        for ip, count in sorted_ips[:5]:
            f.write(f"{ip}: {count} requests\n")

    logging.info("security_incidents.txt created")

except PermissionError:
    logging.error("Cannot write security_incidents.txt")

try:
    with open("error_log.txt", "w") as f:
        f.write("=== HTTP ERROR LOG ===\n\n")
        f.write(f"Total errors: {len(error_entries)}\n\n")
        for entry in error_entries:
            f.write(entry + "\n")

    logging.info("error_log.txt created")

except PermissionError:
    logging.error("Cannot write error_log.txt")

print(f"\nAnalysis complete!")
print(f"Security incidents found: {len(security_incidents)}")
print(f"HTTP errors found: {len(error_entries)}")
print(f"Unique IPs: {len(ip_request_count)}")
print("Reports saved: security_incidents.txt, error_log.txt")
