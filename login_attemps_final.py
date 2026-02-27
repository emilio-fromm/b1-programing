# Copyright by Emilio

login_attempts = [
    ("alice", "success"),
    ("bob", "failed"),
    ("bob", "failed"),
    ("charlie", "success"),
    ("bob", "failed"),
    ("alice", "failed"),
    ("dave", "success"),
    ("eve", "failed"),
    ("eve", "failed"),
    ("eve", "failed"),
    ("eve", "failed")
]

print("Checking login attempts...")
print("deubg - laden der daten")

failed_counts = {}
success_counts = {}

for username, status in login_attempts:
    if status == "failed":
        if username in failed_counts:
            failed_counts[username] = failed_counts[username] + 1
        else:
            failed_counts[username] = 1
    if status == "success":
        if username in success_counts:
            success_counts[username] = success_counts[username] + 1
        else:
            success_counts[username] = 1

print("deubg - counting done, chekcing thresholds")

for username in failed_counts:
    if failed_counts[username] >= 3:
        print("ALERT: User '" + username + "' has " + str(failed_counts[username]) + " failed login attempts")

print("\n=== LOGIN SUMMARY ===")
print("Total login events:", len(login_attempts))
total_failed = sum(failed_counts.values())
total_success = sum(success_counts.values())
print("Total failed logins:", total_failed)
print("Total successful logins:", total_success)

if len(login_attempts) > 0:
    success_rate = round((total_success / len(login_attempts)) * 100, 1)
    print("Success rate:", success_rate, "%")

print("\n=== USER STATUS ===")
all_users = set()
for username, status in login_attempts:
    all_users.add(username)

for user in all_users:
    fails = failed_counts.get(user, 0)
    successes = success_counts.get(user, 0)
    status_label = "OK"
    if fails >= 3:
        status_label = "BLOCKED"
    elif fails >= 1:
        status_label = "WARNING"
    print(f"  {user}: {successes} ok, {fails} failed -> {status_label}")

print("\nSecurity check complete")
