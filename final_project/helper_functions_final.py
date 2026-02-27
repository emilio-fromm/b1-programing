# Copyright by Emilio

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

def load_tasks():
    tasks = []
    if os.path.exists("/Users/emiliofromm/Documents/GitHub/b1-programing/final_project/tasks.txt"):
        print("File found, loading tasks...")

        with open("/Users/emiliofromm/Documents/GitHub/b1-programing/final_project/tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
            return tasks

    else:
        print("File not found!")
        raise HTTPException(status_code=404, detail="File not found")


def save_task(task):
    tasks = []
    print("SAVING TASK: ", task)
    tasks = load_tasks()
    tasks.append(json.dumps(task.__dict__))

    if os.path.exists("/Users/emiliofromm/Documents/GitHub/b1-programing/final_project/tasks.txt"):
        with open("/Users/emiliofromm/Documents/GitHub/b1-programing/final_project/tasks.txt", "w") as file:
            for currentTask in tasks:
                file.write((currentTask) + "\n")
    else:
        print("File not found!")
        raise HTTPException(status_code=404, detail="File not found")

def save_tasks(tasks):

    if os.path.exists("/Users/emiliofromm/Documents/GitHub/b1-programing/final_project/tasks.txt"):
        with open("/Users/emiliofromm/Documents/GitHub/b1-programing/final_project/tasks.txt", "w") as file:
            for currentTask in tasks:
                file.write(currentTask + "\n")
    else:
        print("File not found!")
        raise HTTPException(status_code=404, detail="File not found")
