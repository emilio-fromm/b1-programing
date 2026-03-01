# final project, written and copyright by Emilio Fromm

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os
from pathlib import Path


our_dir = Path(__file__).parent

# Access a file in the same folder
file_path = our_dir / "myfile.txt"
def load_tasks():
    
    tasks = []
    if os.path.exists(our_dir/"tasks.txt"):
        print("found")
        
        with open(our_dir/"tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
            return tasks    
        
    else:
        print("File not found")
        raise HTTPException(status_code=404, detail="File not found")
        
    


def save_task(task):
    tasks = []
    print("DAS IST DIE TASK: ", task)
    tasks = load_tasks()
    tasks.append(json.dumps(task.__dict__))
    
     
    if os.path.exists(our_dir/"tasks.txt"):
        with open(our_dir/"tasks.txt", "w") as file:
            for currentTask in tasks:
                file.write( (currentTask) + "\n")
    else:
        print("File not found")
        raise HTTPException(status_code=404, detail="File not found") 
  
def save_tasks(tasks):
    
    if os.path.exists(our_dir/"tasks.txt"):
        with open(our_dir/"tasks.txt", "w") as file:
            for currentTask in tasks:
                file.write(currentTask + "\n")
    else:
        print("File not found")
        raise HTTPException(status_code=404, detail="File not found")
  
