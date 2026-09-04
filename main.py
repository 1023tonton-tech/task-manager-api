from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str

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

@app.post("/tasks")
def create_task(task: TaskCreate):
        new_task = {
            "id": len(tasks) + 1,
            "title": task.title,
            "completed": False,
        }
        tasks.append(new_task)
        return new_task