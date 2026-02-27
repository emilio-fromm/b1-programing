# Copyright by Emilio
# Final Project - Task Management API with FastAPI
# Tasks are stored as JSON in a .txt file

from fastapi import FastAPI, HTTPException
from helper_functions import load_tasks, save_task, save_tasks
from pydantic import BaseModel
import json
import os

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool


class TaskCreate(BaseModel):
    title: str
    description: str | None = None


@app.get("/")
def root():
    return {"message": "Task Management API running - by Emilio"}

@app.get("/tasks")
def get_all_tasks(completed: bool = None):

    tasks = load_tasks()
    parsedTasks = [json.loads(task) for task in tasks]

    if completed is not None:
        filterdTasks = []
        for task in parsedTasks:
            if task["completed"] == completed:
                filterdTasks.append(task)
        return {"tasks": filterdTasks}
    return {"ALL TASKS": parsedTasks}

@app.get("/first_task")
def get_first_task():
    tasks = load_tasks()
    if len(tasks) != 0:
        return {"task One": json.loads(tasks[0])}
    else:
        raise HTTPException(status_code=404, detail="File is empty, no tasks found")

@app.get("/tasks/stats")
def tasks_stats():
    taskCount = 0
    completedTaskCount = 0
    completedPercentage = 0
    tasks = load_tasks()

    for task in tasks:
        task = json.loads(task)
        if task["completed"] == True:
            completedTaskCount += 1
        taskCount += 1

    if taskCount > 0:
        completedPercentage = (completedTaskCount / taskCount) * 100

    return {
        "Total tasks": taskCount,
        "Completed tasks": completedTaskCount,
        "Pending tasks": taskCount - completedTaskCount,
        "Completion rate": str(completedPercentage) + "%"
    }

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        task = json.loads(task)
        if task["id"] == task_id:
            return {"task": task}
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks")
def post_task(TaskCreating: TaskCreate):
    tasks = load_tasks()
    if tasks:
        newId = max(json.loads(task)["id"] for task in tasks) + 1
    else:
        newId = 1
    print("NEUE ID: ", newId)
    newTask = Task(id=newId, title=TaskCreating.title, description=TaskCreating.description, completed=False)
    save_task(newTask)
    return {"task": newTask}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, TaskCreating: TaskCreate):

    tasks = load_tasks()
    for i, task in enumerate(tasks):
        task = json.loads(task)
        print("task id: ", task["id"], "task id from url: ", task_id)
        if task["id"] == task_id:
            print("task found with ID: ", task_id)

            tasks[i] = json.dumps(Task(id=task_id, title=TaskCreating.title, description=TaskCreating.description, completed=False).__dict__)
            save_tasks(tasks)
            return {"updated task(s)": [json.loads(t) for t in tasks]}

    raise HTTPException(status_code=404, detail="Task with this ID not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    tasks = load_tasks()
    for i, task in enumerate(tasks):
        task = json.loads(task)
        print("task id: ", task["id"], "task id from url: ", task_id)
        if task["id"] == task_id:
            tasks.pop(i)
            save_tasks(tasks)

            return {"updated task(s)": [json.loads(t) for t in tasks]}

    raise HTTPException(status_code=404, detail="Task with this ID not found")


@app.delete("/tasks/")
def delete_tasks():

    tasks = []
    save_tasks(tasks)
    return {"updated task(s)": tasks}
