from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from .db.database import SessionLocal, engine
from .dtos import CreateUserDto
from .services import create_user_service
from . import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/users")
def create_user(create_user_dto: CreateUserDto):
    try:
        session = SessionLocal()
        create_user_service(create_user_dto, session)
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
