# Copyright by Emilio

import json
import os
from fastapi import APIRouter, HTTPException
from schema import UserCreate, User

router = APIRouter()

USERS_FILE = "users.txt"


def read_users():
    print("deubg - lade Benutzer aus Datei")
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        content = f.read()
        if content.strip() == "":
            return []
        return json.loads(content)


def write_users(users):
    print("deubg - speichere Benutzer...")
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


def get_next_id(users):
    if len(users) == 0:
        return 1
    highest_id = max(user["id"] for user in users)
    return highest_id + 1


@router.post("/", response_model=User)
def create_user(user_data: UserCreate):
    users = read_users()
    new_user = {
        "id": get_next_id(users),
        "name": user_data.name,
        "email": user_data.email,
        "age": user_data.age
    }
    users.append(new_user)
    write_users(users)
    print("New user created:", new_user["name"])
    return new_user


@router.get("/", response_model=list[User])
def get_all_users():
    users = read_users()
    return users


@router.get("/search", response_model=list[User])
def search_users(q: str):
    users = read_users()
    results = [u for u in users if q.lower() in u["name"].lower()]
    return results


@router.get("/{id}", response_model=User)
def get_user(id: int):
    users = read_users()
    for user in users:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/{id}", response_model=User)
def update_user(id: int, user_data: UserCreate):
    users = read_users()
    for i, user in enumerate(users):
        if user["id"] == id:
            users[i]["name"] = user_data.name
            users[i]["email"] = user_data.email
            users[i]["age"] = user_data.age
            write_users(users)
            return users[i]
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{id}")
def delete_user(id: int):
    users = read_users()
    for i, user in enumerate(users):
        if user["id"] == id:
            users.pop(i)
            write_users(users)
            return {"message": f"User with ID {id} was deleted"}
    raise HTTPException(status_code=404, detail="User not found")
