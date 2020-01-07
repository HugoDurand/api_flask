from flask import request
from flask_restplus import Namespace, Resource

from ..model.video import Video
from ..util.dto import VideoDto

api = Namespace('elastic', description='elastic operations')
_video = VideoDto.video


@api.route('/search')
class Elasticsearch(Resource):

    @api.doc('search in elasticsearch indexes')
    @api.marshal_list_with(_video)
    @api.response(404, 'video not found.')
    def get(self):
        if not request.args.get('query'):
            api.abort(404)
        video = Video.search(request.args.get('query'))
        return video
