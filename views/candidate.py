from flask import Blueprint, request

from controllers.candidate import *

candidate_view = Blueprint('candidate', __name__, url_prefix='/candidate')

@candidate_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_candidate()
    else:
        submitted_data = request.POST
        files = request.files.getlist("files")

        name, picture, session, position,max_vote = (
            submitted_data['name'], submitted_data['picture'], 
            submitted_data['session'], submitted_data['position'],
            submitted_data['max_vote']
        )

        return save_candidate(name, picture, session, position,max_vote, uploaded_files=files)
    
@candidate_view.route('/<id>', methods=['GET', 'POST'])
def get_or_update_instance(id):
    if request.method == 'GET':
        return get_candidate_with_id(id)
    pass