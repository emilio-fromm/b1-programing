# Copyright by Emilio

import sqlite3

class UserStore:

    def __init__(self, db_path):
        self.db_path = db_path
        print("Initializing database:", db_path)
        self.init_db()

    def init_db(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        connection.commit()
        connection.close()
        print("Table ready!")

    def load(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()
        connection.close()

        users = []
        for row in rows:
            user = {
                "id": row[0],
                "name": row[1],
                "email": row[2]
            }
            users.append(user)
        return users

    def save(self, users):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        for user in users:
            cursor.execute(
                "INSERT OR REPLACE INTO users (id, name, email) VALUES (?, ?, ?)",
                (user["id"], user["name"], user["email"])
            )
        connection.commit()
        connection.close()

    def find_by_id(self, user_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        connection.close()

        if row is None:
            return None

        user = {
            "id": row[0],
            "name": row[1],
            "email": row[2]
        }
        return user

    def update_user(self, user_id, updated_data):
        existing_user = self.find_by_id(user_id)
        if existing_user is None:
            return False

        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        if "name" in updated_data:
            cursor.execute(
                "UPDATE users SET name = ? WHERE id = ?",
                (updated_data["name"], user_id)
            )
        if "email" in updated_data:
            cursor.execute(
                "UPDATE users SET email = ? WHERE id = ?",
                (updated_data["email"], user_id)
            )

        connection.commit()
        connection.close()
        return True

    def delete_user(self, user_id):
        existing_user = self.find_by_id(user_id)
        if existing_user is None:
            return False

        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        connection.commit()
        connection.close()
        return True
