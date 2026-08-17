from fastapi import FastAPI

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