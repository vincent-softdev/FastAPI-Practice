from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import models
from db.database import SessionLocal, engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    
    try:
        # First return is db
        yield db
    finally:
        # Second time this method is called, we have db.close()
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def read_all(db: db_dependency):
    return db.query(models.Todos).all()

@app.get("/todo/{todo_list}")
async def read_todo(db: db_dependency, todo_id: int):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")
