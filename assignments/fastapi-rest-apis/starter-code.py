from typing import List

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI Tasks API")


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    done: bool = False


class Task(TaskCreate):
    id: int


# In-memory storage for assignment practice.
tasks: List[Task] = []


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return tasks


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate):
    task = Task(id=len(tasks) + 1, **payload.model_dump())
    tasks.append(task)
    return task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")
