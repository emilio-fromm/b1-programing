# Copyright by Emilio

devices = [
    ("192.168.1.10", [22, 80, 443]),
    ("192.168.1.11", [21, 22, 80]),
    ("192.168.1.12", [23, 80, 3389]),
    ("192.168.1.13", [8080, 3306, 22])
]

risky_ports = [21, 23, 3389, 3306]

port_descriptions = {
    21: "FTP - unencrypted file transfer",
    23: "Telnet - unencrypted remote access",
    3389: "RDP - Remote Desktop Protocol",
    3306: "MySQL - database port exposed"
}

print("Scanning network devices...")
print("deubg - loaded", len(devices), "Geraete")

risk_count = 0
device_risk_scores = {}

for ip, open_ports in devices:
    device_risk = 0
    for port in open_ports:
        if port in risky_ports:
            desc = port_descriptions.get(port, "unknown risk")
            print("WARNING: " + ip + " has risky port " + str(port) + " open (" + desc + ")")
            risk_count = risk_count + 1
            device_risk = device_risk + 1
    device_risk_scores[ip] = device_risk

print("\n=== DEVICE RISK SUMMARY ===")
for ip, score in device_risk_scores.items():
    if score == 0:
        level = "SAFE"
    elif score == 1:
        level = "LOW RISK"
    elif score == 2:
        level = "MEDIUM RISK"
    else:
        level = "HIGH RISK"
    print(f"  {ip}: {score} risky port(s) -> {level}")

print("\nScan complete: " + str(risk_count) + " security risks found")
