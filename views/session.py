from flask import Blueprint, request, Response

from controllers.session import *
from models.exceptions import ModelNotFoundError

session_view = Blueprint('session', __name__, url_prefix='/session')

@session_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_session()
    else:
        submitted_data = request.POST

        return Response(save_session(submitted_data['name']), status=201)

@session_view.route('/<id>', methods=['GET', 'POST', 'DELETE'])
def get_or_update_instance(id):
    if request.method == 'GET':
        try:
            return get_session_with_id(id)
        except ModelNotFoundError:
            return Response("<h1>Instance not found</h1>", status=404)
    elif request.method == 'PATCH':
        data = request.PATCH
        return Response(save_session(name=data['name']), status=201)
    elif request.method == 'DELETE':
        return Response(delete_session(id), status=201)
