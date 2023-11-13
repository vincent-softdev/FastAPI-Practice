from typing import Optional
from pydantic import BaseModel

class UserModel(BaseModel):
    email: Optional[str]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    hashed_password: Optional[str]
    is_active : Optional[bool]
    role : Optional[str]

class CreateUserModel(UserModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    role: str

class UserDB(UserModel):
    id: Optional[int]

users = UserDB