from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from models import users
import passlib.context import CryptContext

# app = FastAPI()
router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

class CreateUserRequest(BaseModel):
    username: str
    email: str 
    first_name: str
    last_name: str
    password: str
    role: str

@router.post("/auth/", status_code=status.HTTP_201_CREATED)
async def.create_user(DB: db_dependency, CreateUserRequest: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )
    db.add(create_user_model)
    db.commit()
    

