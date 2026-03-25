from fastapi import FastApi

app = FastAPI()

# async is added behind the scenes as well
@app.get("/api-endpoint")
async def first_api():
    return {'message':'Hello Eric!'}

# address: 127.0.0.1:8000/api-endpoint

BOOKS = []

@app.get("/books")
async def read_all_books():
    return BOOKS

# 127.0.0.1:8000/books