# Copyright by Emilio

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from user_store import UserStore
import uuid

app = FastAPI()

class UserInput(BaseModel):
    name: str
    email: str

class UserUpdateInput(BaseModel):
    name: str = None
    email: str = None

store = UserStore("users.db")


@app.get("/users")
def get_users():
    print("deubg - Benutzer werden aus Datenbank geladen")
    users = store.load()
    return users


@app.post("/users")
def create_user(user_input: UserInput):
    new_user = {
        "id": str(uuid.uuid4()),
        "name": user_input.name,
        "email": user_input.email
    }
    store.save([new_user])
    print("New user saved to DB:", new_user["name"])
    return new_user


@app.get("/users/{user_id}")
def get_user(user_id: str):
    user = store.find_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/users/{user_id}")
def update_user(user_id: str, user_input: UserUpdateInput):
    updated_data = {}
    if user_input.name is not None:
        updated_data["name"] = user_input.name
    if user_input.email is not None:
        updated_data["email"] = user_input.email

    success = store.update_user(user_id, updated_data)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User successfully updated"}


@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    success = store.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User successfully deleted"}
