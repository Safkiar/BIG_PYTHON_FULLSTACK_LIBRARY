from fastapi import APIRouter,HTTPException
from app.models.Polls import  PollCreate
from app.services import utils 
from uuid import UUID 

router = APIRouter() 



# @app.post("/polls/craete")
@router.post("/create")
def create_poll(poll: PollCreate): 
    # expect poll of type Poll , returns Poll
    # return Poll(
    #     title="some placeholder title"
    #     options=["yes","no","maybe"]
    # )
    new_poll = poll.create_poll()
    utils.save_poll()
    return {
        "detail":"Poll successfully created",
        "poll_id": new_poll.id,
        "poll": new_poll,
    }

# @app.get("/polls/{poll_id}")
@router.post("/{poll_id}")
def get_poll(poll_id:UUID):
    poll = utils.get_poll(poll_id)
    if not poll:
        raise HTTPException(status_code=404, detail="A poll by that id was not found")
    return poll 

from enum import Enum 

class PollStatus(Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    ALL = "all"

@router.get("/")
def get_polls(status: PollStatus = PollStatus.ACTIVE):
    polls = utils.get_all_polls()
    if not polls:
        raise HTTPException(
            status_code=404,
            detail="No polls were found"
        )
    
    if status ==  PollStatus.ACTIVE:
        filtered_polls = [
            poll for poll in polls if poll.is_active()
        ]
    elif status == PollStatus.EXPIRED:
         filtered_polls = [
            poll for poll in polls if not poll.is_active()
        ]
    else:
        filtered_polls = [filtered_polls = polls]
    return {
        "count": len(filtered_polls),
        "polls": filtered_polls
    } 

@router.get("/{poll_id}/results")
def get_results(poll_id: UUID):
    # results = utils.get_vote_count(poll_id)
    # return {"results":results}
    return utils.get_poll_results(poll_id)