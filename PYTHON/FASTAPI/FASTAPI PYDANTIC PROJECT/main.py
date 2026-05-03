from fastapi import FastAPI
from app.api import polls, votes, danger, exceptions
from fastapi.exceptions import RequestValidationError


app = FastAPI(
    title="Polls API",
    description="A simple API to create and vote on piolls",
    version="0.1",
    openai_tags=[
        {
            "name":"polls",
            "description":"Operations related to creating and viewing polls"
        },
           {
            "name":"danger",
            "description":"Operations related to deleting votes"
        },
          {
            "name":"votes",
            "description":"Operations related to creating and viewing votes"
        }
    ]
)

from fastapi.exceptions import RequestValidationError

app.add_exception_handler(RequestValidationError, exceptions.custom )
app.include_router(polls.router, prefix="/polls", tags=["polls"])
app.include_router(danger.router, prefix="/polls", tags=["danger"])
app.include_router(votes.router, prefix="/vote", tags=["votes"])

@app.get("/test")
def test():
    return {"message":"hello there"}



### connect to reddis 
###
###

# @app.post("/redis/save", tags=["throwaway"])
# def save_Redis(id:str, name: str):
#     redis_client.set(id, name)
#     return {"status":"success"}

# @app.get("/redis/get/{id}",tags=["throwaway"])
# def get_redis(id:str)
#     name = redis_client.get(id)
#     return {"id":id,"name":name}

###
###
###

