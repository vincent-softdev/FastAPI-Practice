from fastapi import APIRouter
from models import Users
from schemas import CreateUserModel

router = APIRouter()

@router.get("")
async def get_all_users():
    return None

# create new user
@router.post("/")
async def create_user(create_user_request: CreateUserModel):
    create_user_model = Users(
        email = create_user_request.email,
        username = create_user_request.username,
        first_name = create_user_request.first_name,
        last_name = create_user_request.last_name,
        hashed_password = create_user_request.password,
        is_active = True,
        role = create_user_request.role
    )

    
    return create_user_model
