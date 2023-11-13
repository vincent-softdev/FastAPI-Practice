from typing import Optional
from pydantic import BaseModel

class TodosModel(BaseModel):
    title: Optional[str]
    description: Optional[str]
    priority: Optional[int]
    complete: Optional[bool]

class CreateTodosModel(TodosModel):
    title: str
    priority: str
    complete: str

class TodosDB(TodosModel):
    id: int
    owner_id: int

todos = TodosDB