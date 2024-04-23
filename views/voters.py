from flask import Blueprint, request, Response

from controllers.voters import *
from models.exceptions import ModelNotFoundError

voters_view = Blueprint('voters', __name__, url_prefix='/voters')

@voters_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_voters()
    elif request.method == 'POST':
        submitted_data = request.form
        # Assuming submitted_data contains necessary fields for creating a voter
        voter_name = submitted_data.get('name')
        if voter_name:
            saved_voter_id = save_voter(voter_name)
            return Response(f"Voter {voter_name} saved with ID: {saved_voter_id}", status=201)
        else:
            return Response("Missing required field: 'name'", status=400)

@voters_view.route('/<id>', methods=['GET', 'PATCH', 'DELETE'])
def get_or_update_instance(id):
    if request.method == 'GET':
        try:
            return get_voter_with_id(id)
        except ModelNotFoundError:
            return Response("<h1>Instance not found</h1>", status=404)
    elif request.method == 'PATCH':
        data = request.form
        voter_name = data.get('name')
        if voter_name:
            saved_voter_id = update_voter(id, voter_name)
            return Response(f"Voter {voter_name} updated with ID: {saved_voter_id}", status=200)
        else:
            return Response("Missing required field: 'name'", status=400)
    elif request.method == 'DELETE':
        return Response(delete_voters(id), status=204)