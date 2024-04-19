import os

from models.candidate import Candidate


from werkzeug.utils import secure_filename

from constants import UPLOAD_FOLDER

def get_all_candidate():
    return Candidate.read()

def get_candidate_with_id(id):
    return Candidate.read(id)

def save_candidate(name, picture, session, position,max_vote, id=None, uploaded_files=None):
    if id != None:
        candidate = get_candidate_with_id(id)
        candidate.name, candidate.picture, candidate.session, candidate.position,candidate.max_vote = (
           name, picture, session, position,max_vote
        )
    else:
       candidate= Candidate(
            name=name, picture=picture, session=session, position=position, max_vote=max_vote
        )

    Candidate.save()

    return candidate
    
def delete_candidate(id):
    Candidate = get_candidate_with_id(id)
    Candidate.delete()