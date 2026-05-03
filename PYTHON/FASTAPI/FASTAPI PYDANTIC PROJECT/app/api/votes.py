from fastapi import APIRouter, HTTPException, Depends
from uuid import UUID 
from app.models.Votes import VoteById, VoteByLabel, Vote, Voter
from app.models.Polls import Poll
from app.services import utils 
from typing import Union

router = APIRouter() 

def common_validations(poll_id:UUID, vote: Union[VoteById, VoteByLabel]):
    poll = utils.get_poll(poll_id)
    voter_email = vote.voter.email 

    if not poll():
        raise HTTPException(
            status_code=404,
            detail="the poll was not found"
            )

    if not poll.is_active():
           raise HTTPException(
              status_code=400,
              detail="the poll is expired"
         )
    if utils.get_vote(poll_id,vote.voter.email):
         raise HTTPException(
              status_code=400,
              detail="already voted"
         )
    return poll

@router.post("/{poll_id}/id")
def vote_by_id(poll_id:UUID, vote: VoteById, VoteByLabel, poll: Poll = Depends(common_validations)):
    poll = utils.get_poll(poll_id)


    if vote.choice_id not in [choice.id for choice in poll.options]:
         raise HTTPException(
              status_code=400,
              detail="Invalid choice"
         )

    vote = Vote(
        poll_id=poll_id,
        choice_id=vote.choice_id,
        voter=Voter(
            **vote.voter.model_dump()
        )
    )
    utils.save_vote(poll_id, vote)
    return {"message":"Vote recorded","vote":vote}

@router.post("/{poll_id}/label")
def vote_by_id(poll_id:UUID, vote: VoteByLabel, poll: Poll = Depends(common_validations)):
    poll = utils.get_poll(poll_id)
    # choice_id = utils.get_choice_id_by_label(
    #       poll_id,
    #       vote.choice_label
    #  )
    choice_id = utils.get_choice_id_by_label_given(
          poll, vote.choice_label)
    if not choice_id:
          raise HTTPException(
               status_code=400,
               detail="invalid"
          )
    vote = Vote(
        poll_id=poll_id,
        choice_id=choice_id,
        voter=Voter(
            **vote.voter.model_dump()
        ))
     
    utils.save_vote(poll_id, vote)

    return {"message":"Vote recorded","vote":vote}



