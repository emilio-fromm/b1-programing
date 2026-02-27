# Copyright by Emilio

from datetime import datetime, timedelta
import random


class Device:
    def __init__(self, device_id, device_type, owner, firmware_version="1.0.0"):
        self.__device_id = device_id
        self.__device_type = device_type
        self.__firmware_version = firmware_version
        self.__compliance_status = "unknown"
        self.__owner = owner
        self.__last_security_scan = None
        self.__is_active = True
        self.__access_log = []
        self.__uptime_days = random.randint(1, 365)
        self.__battery_level = random.randint(10, 100)

    def authorise_access(self, user):
        if not self.__is_active:
            self.__access_log.append(f"{user.get_username()} - Denied: Device inactive")
            return False

        if self.__compliance_status != "compliant":
            if not user.check_privileges("admin"):
                self.__access_log.append(f"{user.get_username()} - Denied: Device not compliant")
                return False

        if self.__owner != user.get_username() and not user.check_privileges("admin"):
            self.__access_log.append(f"{user.get_username()} - Denied: Not the owner")
            return False

        self.__access_log.append(f"{user.get_username()} - Access granted")
        return True


    def run_security_scan(self):
        self.__last_security_scan = datetime.now()
        self.__compliance_status = "compliant"
        self.__access_log.append("Security scan completed")

    def check_compliance(self):
        if self.__last_security_scan is None:
            self.__compliance_status = "unknown"
            return False

        days_since_scan = (datetime.now() - self.__last_security_scan).days
        if days_since_scan > 30:
            self.__compliance_status = "non-compliant"
            return False

        return self.__compliance_status == "compliant"


    def update_firmware(self, version, user):
        if not user.check_privileges("admin"):
            return False
        self.__firmware_version = version
        self.__access_log.append(f"{user.get_username()} updated firmware to {version}")
        return True

    def quarantine(self, user):
        if not user.check_privileges("admin"):
            return False
        self.__is_active = False
        self.__access_log.append(f"{user.get_username()} quarantined the device")
        return True


    def get_health_score(self):
        print("deubg - calucating health score")
        score = 100
        if not self.__is_active:
            score = score - 50
        if self.__compliance_status != "compliant":
            score = score - 30
        if self.__battery_level < 20:
            score = score - 10
        if self.__uptime_days > 300:
            score = score - 10
        return max(0, score)

    def get_device_info(self):
        return {
            "device_id": self.__device_id,
            "device_type": self.__device_type,
            "firmware_version": self.__firmware_version,
            "compliance_status": self.__compliance_status,
            "owner": self.__owner,
            "is_active": self.__is_active,
            "battery_level": self.__battery_level,
            "uptime_days": self.__uptime_days
        }

    def get_id(self):
        return self.__device_id



class DeviceManager:
    def __init__(self):
        self.__devices = {}

    def add_device(self, device):
        self.__devices[device.get_id()] = device
        print(f"Device {device.get_id()} added")

    def remove_device(self, device_id, user):
        if not user.check_privileges("admin"):
            print("Access denied: admin required")
            return False
        if device_id in self.__devices:
            del self.__devices[device_id]
            print(f"Device {device_id} removed")
            return True
        print("Device not found")
        return False


    def generate_security_report(self, user):
        if not user.check_privileges("admin"):
            print("Access denied: admin required")
            return None
        print("\n=== SECURITY REPORT ===")
        for device_id, device in self.__devices.items():
            info = device.get_device_info()
            compliant = device.check_compliance()
            health = device.get_health_score()
            print(f"Device: {info['device_id']} | Type: {info['device_type']} | "
                  f"Owner: {info['owner']} | Compliant: {compliant} | Active: {info['is_active']} | "
                  f"Battery: {info['battery_level']}% | Health: {health}/100")


class User:
    def __init__(self, username, password, privilege_level="standard"):
        self.__username = username
        self.__password_hash = "hashed_" + password
        self.__privilege_level = privilege_level

    def check_privileges(self, required_level):
        hierarchy = {"guest": 0, "standard": 1, "admin": 2}
        return hierarchy.get(self.__privilege_level, 0) >= hierarchy.get(required_level, 0)

    def get_username(self):
        return self.__username


print("=== IoT Device Manager Test ===\n")

admin = User("admin", "admin123", "admin")
alice = User("alice", "secret99", "standard")

manager = DeviceManager()

laptop = Device("DEV001", "Laptop", "alice")
router = Device("DEV002", "Router", "admin")

manager.add_device(laptop)
manager.add_device(router)

print("\n--- Security Scan on Laptop ---")
laptop.run_security_scan()
print("Compliance after scan:", laptop.check_compliance())
print("Laptop health score:", laptop.get_health_score(), "/100")

print("\n--- Alice tries to access Laptop ---")
print("Access granted:", laptop.authorise_access(alice))

print("\n--- Alice tries to access Router ---")
print("Access granted:", router.authorise_access(alice))

print("\n--- Admin accesses Router ---")
print("Access granted:", router.authorise_access(admin))

print("\n--- Admin updates Firmware ---")
print("Firmware updated:", laptop.update_firmware("2.0.1", admin))
print("Alice tries firmware:", laptop.update_firmware("3.0.0", alice))

print("\n--- Admin quarantines Router ---")
print("Quarantine:", router.quarantine(admin))
print("Router info:", router.get_device_info())

manager.generate_security_report(admin)
