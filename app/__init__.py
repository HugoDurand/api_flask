from flask_restplus import Api
from flask import Blueprint

from .main.controller.auth_controller import api as auth_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.video_controller import api as video_ns
from .main.controller.comment_controller import api as comment_ns
from .main.controller.category_controller import api as category_ns
from .main.controller.elastic_controller import api as elastic_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK API',
          version='1.0',
          description='Flask Api Documentation'
          )

api.add_namespace(auth_ns)
api.add_namespace(user_ns, path='/user')
api.add_namespace(video_ns, path='/video')
api.add_namespace(comment_ns, path='/comment')
api.add_namespace(category_ns, path='/category')
api.add_namespace(elastic_ns, path='/elastic')
