from flask_restplus import Namespace, fields
from datetime import time

class UserDto:
    api = Namespace('user', description='user operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'firstName': fields.String(required=True, description='user firstName'),
        'lastName': fields.String(required=True, description='user lastName'),
        'password': fields.String(required=True, description='user password')
    })

class AuthDto:
    api = Namespace('auth', description='authentication operations')
    user_auth = api.model('auth', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class VideoDto:
    api = Namespace('video', description='video operations')
    video = api.model('video',{
        'title': fields.String(required=True, description='video title'),
        'link': fields.String(required=True, description='video link'),
        'duration': fields.DateTime(),
    })

class CommentDto:
    api = Namespace('comment', description='comment operations')
    comment = api.model('comment', {
        'text': fields.String(required=True, description='The text comment'),
        'video_id': fields.Integer(required=True, description='The Video ID'),
    })