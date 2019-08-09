from flask import request
from flask_restplus import Resource

from ..util.dto import VideoDto
from ..service.video_service import new_video, get_videos, get_video
from ..util.decorator import token_required

api  = VideoDto.api
_video = VideoDto.video


@api.route('/')
class getOrPostVideo(Resource):

    @api.doc('list all videos')
    @api.marshal_list_with(_video, envelope='data')
    def get(self):
        return get_videos()
    
    @api.response(201, 'Video successfully created.')
    @api.doc('create a new video')
    @api.expect(_video, validate=True)
    def post(self):
        data = request.json
        return new_video(data=data)

@api.route('/<id>')
@api.param('id', 'video identifier')
class getVideoById(Resource):

    @api.response(404, 'Video not found.')
    @api.doc('get a video')
    @api.marshal_list_with(_video)
    def get(self, id):
        video = get_video(id)
        if not video:
            api.abort(404)
        else:
            return video