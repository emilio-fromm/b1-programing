# Copyright by Emilio

from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int
