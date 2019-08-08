from flask_restplus import Namespace, fields
from datetime import time

class TimeFormat(fields.Raw):
    def format(self, value):
        return time.strftime(value, "%H:%M:%S")

class UserDto:
    api = Namespace('user', description='user operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'fistName': fields.String(required=True, description='user firstName'),
        'lastName': fields.String(required=True, description='user lastName'),
        'password': fields.String(required=True, description='user password')
    })

class AuthDto:
    api = Namespace('auth', description='authentication operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class VideoDto:
    api = Namespace('video', description='video operations')
    video = api.model('video',{
        'title': fields.String(required=True, description='video title'),
        'link': fields.String(required=True, description='video link'),
        'duration': TimeFormat(required=True, description='video duration')
    })