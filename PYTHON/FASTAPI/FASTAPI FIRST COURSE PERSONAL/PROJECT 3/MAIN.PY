from fastapi import FastAPI, Path, Depends, HTTPException
import models
from database import engine, Sessionlocal
from typing import Annotated 
from sqlalchemy.orm import Session
from models import todos
from starlette import status
from pydantic import BaseModel, Field
from routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
