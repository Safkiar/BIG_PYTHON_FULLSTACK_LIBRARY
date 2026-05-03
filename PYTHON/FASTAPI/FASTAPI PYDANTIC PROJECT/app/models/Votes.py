from pydantic import BaseModel, EmailStr, Field 
from uuid import UUID 
from datetime import datetime 

class VoterCreate(BaseModel):
    """ WRITE MODEL """
    email: EmailStr

class Voter(VoterCreate):
    """ READ MODEL"""
    voted_at: datetime = Field(default_factory=datetime.now)

class Vote(BaseModel):
    """the vore read model"""
    poll_id: UUID 
    choice_id: UUID
    voter: Voter

class VoteById(BaseModel):
    choice_id: UUID
    voter: VoterCreate

class VoteByLabel(BaseModel):
    choice_label: int 
    voter: VoterCreate 
