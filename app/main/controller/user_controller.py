from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import new_user, get_users, get_user
from ..util.decorator import token_required

api = UserDto.api
_user = UserDto.user


@api.route('/')
class getOrPostUser(Resource):

    @api.doc('list all users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        return get_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return new_user(data=data)

@api.route('/<id>')
@api.param('id', 'user identifier')
class getUserById(Resource):

    @api.response(404, 'User not found.')
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, id):
        user = get_user(id)
        if not user:
            api.abort(404)
        else:
            return user