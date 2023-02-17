from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from src.dtos import CreateUserDto


app = FastAPI()

users = []


@app.post("/users")
def create_user(create_user_dto: CreateUserDto):
    if create_user_dto.username in users:
        raise HTTPException(status_code=400, detail="Username already exists")
    users.append(create_user_dto.username)
    return {"message": "User created successfully"}
