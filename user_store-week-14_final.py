# Copyright by Emilio

import json

class UserStore:

    def __init__(self, file_path):
        self.file_path = file_path
        print("UserStore initialized with file:", file_path)

    def load(self):
        users = []
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if line != "":
                        user = json.loads(line)
                        users.append(user)
        except FileNotFoundError:
            users = []
        return users

    def save(self, users):
        with open(self.file_path, "w") as file:
            for user in users:
                line = json.dumps(user)
                file.write(line + "\n")

    def find_by_id(self, user_id):
        users = self.load()
        for user in users:
            if user["id"] == user_id:
                return user
        return None

    def update_user(self, user_id, updated_data):
        users = self.load()
        found = False
        for i in range(len(users)):
            if users[i]["id"] == user_id:
                users[i].update(updated_data)
                found = True
                break
        if found:
            self.save(users)
            return True
        return False

    def delete_user(self, user_id):
        users = self.load()
        new_users = []
        found = False
        for user in users:
            if user["id"] == user_id:
                found = True
            else:
                new_users.append(user)
        if found:
            self.save(new_users)
            return True
        return False
