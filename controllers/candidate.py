import os
from models.candidate import Candidate

def get_all_candidates():
    return Candidate.read()

def get_candidate_with_id(id):
    return Candidate.read(id)

def save_candidate(name, picture, session, position, max_vote, id=None, uploaded_files=None):
    if id is not None:
        candidate = get_candidate_with_id(id)
        candidate.name = name
        candidate.picture = picture
        candidate.session = session
        candidate.position = position
        candidate.max_vote = max_vote
    else:
        candidate = Candidate(
            name=name, picture=picture, session=session, position=position, max_vote=max_vote
        )

    candidate.save()

    return candidate
    
def delete_candidate(id):
    candidate = Candidate.read(id)
    if candidate:
        candidate.delete()
        return candidate.toJSON()
    else:
        return None