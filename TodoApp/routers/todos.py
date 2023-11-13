from fastapi import APIRouter
from typing import Annotated, List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from models import models
import schemas
from db.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    
    try:
        # First return is db
        yield db
    finally:
        # Second time this method is called, we have db.close()
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("", response_model=List[schemas.todos])
async def read_all(db: db_dependency):
    return db.query(models.Todos).all()

@router.get("/todo/{todo_list}", response_model=schemas.todos)
async def read_todo(db: db_dependency, todo_id: int):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")
