from flask import request, jsonify
from ..model.video import Video
from flask_restplus import Namespace, Resource
from ..util.dto import VideoDto

from ..service.elastic_service import query_index

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
