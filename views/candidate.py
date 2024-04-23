from flask import Blueprint, request, Response

from controllers.candidate import *

candidate_view = Blueprint('candidate', __name__, url_prefix='/candidate')

@candidate_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        # Get all candidates
        return get_all_candidates()
    elif request.method == 'POST':
        # Create a new candidate
        submitted_data = request.form
        files = request.files.getlist("files") 

        name = submitted_data.get('name')
        picture = submitted_data.get('picture')
        session = submitted_data.get('session')
        max_vote = submitted_data.get('max_vote')

        # Check for required fields
        if not all([name, picture, session, max_vote]):
            return Response("Missing required fields", status=400)

        return save_candidate(name, picture, session, max_vote, uploaded_files=files)

@candidate_view.route('/<id>', methods=['GET', 'PUT', 'DELETE'])
def get_or_update_instance(id):
    if request.method == 'GET':
        # Get candidate by ID
        return get_candidate_with_id(id)
    elif request.method == 'DELETE':
        # Delete candidate by ID
        return delete_candidate(id)
    elif request.method == 'PUT':  # Assuming this is for updating the instance
        # Update candidate by ID
        submitted_data = request.form
        files = request.files.getlist("files") 

        name = submitted_data.get('name')
        picture = submitted_data.get('picture')
        session = submitted_data.get('session')
        max_vote = submitted_data.get('max_vote')

        # Check for required fields
        if not all([name, picture, session, max_vote]):
            return Response("Missing required fields", status=400)

        return update_candidate(id, name, picture, session, max_vote, uploaded_files=files)