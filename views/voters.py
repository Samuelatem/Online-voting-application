from flask import Blueprint, request, Response

from controllers.voters import *
from models.exceptions import ModelNotFoundError

voters_view = Blueprint('voters', __name__, url_prefix='/voters')

@voters_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_voters()
    else:
        submitted_data = request.POST

        return Response(save_voters(submitted_data['name']), status=201)

@voters_view.route('/<id>', methods=['GET', 'POST', 'DELETE'])
def get_or_update_instance(id):
    if request.method == 'GET':
        try:
            return get_voters_with_id(id)
        except ModelNotFoundError:
            return Response("<h1>Instance not found</h1>", status=404)
    elif request.method == 'PATCH':
        data = request.PATCH
        return Response(save_voters(name=data['name']), status=201)
    elif request.method == 'DELETE':
        return Response(delete_voters(id), status=201)
