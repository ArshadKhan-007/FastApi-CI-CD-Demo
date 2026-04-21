from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import time

app = FastAPI()
db = []

class Task(BaseModel):
    name: str
    priority: int

def heavy_processing(task_name: str):
    # Simulates a background job
    print(f"Starting heavy processing for: {task_name}")
    time.sleep(5)
    print(f"Finished processing: {task_name}")

@app.get("/")
def read_root():
    return {"status": "System Online", "tasks_count": len(db)}

@app.post("/tasks")
def create_task(task: Task, background_tasks: BackgroundTasks):
    db.append(task)
    background_tasks.add_task(heavy_processing, task.name)
    return {"message": "Task received and processing in background", "task": task}

@app.get("/analytics")
def get_analytics():
    high_priority = [t for t in db if t.priority > 5]
    return {
        "total_tasks": len(db),
        "high_priority_count": len(high_priority)
    }

@app.get("/health")
def health_check():
    return {"status" : "Green..!Good to go.."}

@app.get("/about")
def about():
    return {"message" : "This is a simple FastAPI application for demonstration purposes.."}

@app.get('/contact')
def contact():
    return {"message" : "This is a simple FastAPI application for demonstration purposes.."}

