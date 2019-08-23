from flask import request
from flask_restplus import Resource

from ..util.dto import CommentDto
from ..service.comment_service import new_comment, get_comments, get_comment
from ..util.decorator import token_required

api  = CommentDto.api
_comment = CommentDto.comment


@api.route('/')
class getOrPostComment(Resource):

    @api.doc('list all comments')
    @api.marshal_list_with(_comment, envelope='data')
    def get(self):
        return get_comments()
    
    @api.response(201, 'Comment successfully created.')
    @api.doc('create a new comment')
    @api.expect(_comment, validate=True)
    def post(self):
        data = request.json
        return new_comment(data=data)

@api.route('/<id>')
@api.param('id', 'comment identifier')
class getCommentById(Resource):

    @api.response(404, 'comment not found.')
    @api.doc('get a comment')
    @api.marshal_list_with(_comment)
    def get(self, id):
        comment = get_comment(id)
        if not comment:
            api.abort(404)
        else:
            return comment