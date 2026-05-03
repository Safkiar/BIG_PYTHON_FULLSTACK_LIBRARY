from pydantic import BaseModel
from typing import List

class Result(BaseModel):
    description: str 
    vote_count: int

class Pollresults(BaseModel):
    title: str
    total_votes: int 
    results: List[Result]