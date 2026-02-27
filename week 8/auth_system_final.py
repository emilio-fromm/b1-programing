# Copyright by Emilio

from datetime import datetime


class User:
    def __init__(self, username, password, privilege_level="standard"):
        self.__username = username
        self.__password_hash = "hashed_" + password
        self.__privilege_level = privilege_level
        self.__login_attempts = 0
        self.__account_status = "active"
        self.__activity_log = []
        self.__last_login = None
        self.__session_token = None

    def __hash_password(self, password):
        return "hashed_" + password


    def authenticate(self, password):
        if self.__account_status == "locked":
            self.__activity_log.append("Login attempt on locked account")
            return False

        if self.__hash_password(password) == self.__password_hash:
            self.__login_attempts = 0
            self.__last_login = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.__session_token = "tok_" + self.__username + "_" + str(hash(password + self.__last_login))
            self.__activity_log.append(f"Successful login at {self.__last_login}")
            return True
        else:
            self.__login_attempts = self.__login_attempts + 1
            self.__activity_log.append(f"Failed login attempt {self.__login_attempts}")
            if self.__login_attempts >= 3:
                self.lock_account()
            return False

    def check_privileges(self, required_level):
        hierarchy = {"guest": 0, "standard": 1, "admin": 2}
        user_level = hierarchy.get(self.__privilege_level, 0)
        needed_level = hierarchy.get(required_level, 0)
        return user_level >= needed_level


    def lock_account(self):
        self.__account_status = "locked"
        self.__session_token = None
        self.__activity_log.append("Account locked after too many failed attempts")

    def reset_login_attempts(self, admin_password):
        if self.__hash_password(admin_password) == "hashed_admin123":
            self.__account_status = "active"
            self.__login_attempts = 0
            self.__activity_log.append("Account unlocked by admin")
            return True
        return False


    def get_session_token(self):
        return self.__session_token

    def get_safe_info(self):
        return {
            "username": self.__username,
            "privilege_level": self.__privilege_level,
            "account_status": self.__account_status,
            "last_login": self.__last_login
        }

    def get_username(self):
        return self.__username

    def get_privilege_level(self):
        return self.__privilege_level



admin = User("herr_schneider", "admin123", "admin")
lukas = User("lukas_meier", "secret99", "standard")
sarah = User("sarah_w", "guest01", "guest")

print("--- Korrekte Anmeldung / correct login ---")
print("Lukas login:", lukas.authenticate("secret99"))
print("Session token:", lukas.get_session_token())

print("\n--- Falsches Passwort (3x für Sperrung)  / wrong password ---")
print("Lukas wrong:", lukas.authenticate("wrongpassword"))
print("Lukas wrong:", lukas.authenticate("wrongpassword"))
print("Lukas wrong:", lukas.authenticate("wrongpassword"))

print("\nLukas account overview:", lukas.get_safe_info())

print("\n--- Admin entsperrt Konto / admin unlocks account---")
print("unlocked:", lukas.reset_login_attempts("admin123"))
print("Lukas after:", lukas.get_safe_info())

print("\n--- Rechteprüfung / privilege control---")
print("Admin has admin controls:", admin.check_privileges("admin"))
print("Sarah has admin privileges:", sarah.check_privileges("admin"))
print("Lukas has standard rights:", lukas.check_privileges("standard"))

print("Last Login Admin:", admin.get_safe_info()["last_login"])
