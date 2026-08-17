from fastapi import FastAPI
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

@app.post("/tasks")
def create_task(task: TaskCreate):
        new_task = {
            "id": len(tasks) + 1,
            "title": task.title,
            "completed": False,
        }
        tasks.append(new_task)
        return new_task