from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    completed: bool

app = FastAPI()
tasks = [
    {
        "id": 1,
        "title": "レポートを提出する",
        "completed": False,
    }
]
@app.get("/")
def read_root():
    return {"message": "Task Manager API"}


@app.get("/tasks")
def read_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")

@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = task_update.completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks")
def create_task(task: TaskCreate):
        new_task = {
            "id": len(tasks) + 1,
            "title": task.title,
            "completed": False,
        }
        tasks.append(new_task)
        return new_task