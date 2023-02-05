from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from src.dtos import CreateTaskDTO
from src.models import Task


app = FastAPI()

created_tasks = []

@app.post("/tasks/")
def create_task(create_task_dto: CreateTaskDTO) -> Task:
    new_task = Task(
        id=len(created_tasks) + 1,
        title=create_task_dto.title,
        description=create_task_dto.description,
        tags=create_task_dto.tags,
        completed=False,
    )
    created_tasks.append(new_task)
    return new_task

@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> Task:
    try:
        return created_tasks[task_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="Not Found")
